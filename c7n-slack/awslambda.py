#!/usr/bin/env python

from __future__ import print_function

import boto3
import json
import logging
import os
import requests
import time
import zlib

from base64 import b64decode

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    sqs = boto3.resource('sqs')
    c7n = sqs.get_queue_by_name(QueueName='c7nMessageQueue')
    attempts = 0

    while attempts < 4:
        messages = c7n.receive_messages(
        AttributeNames=['All'],
        MaxNumberOfMessages=10,
        MessageAttributeNames=['All'])

        # AWS may have answered from a server that doesn't have our
        # messages. So sleep and then try again.
        if len(messages) == 0:
            time.sleep(1)
            attempts = attempts + 1
            continue

        for message in messages:

            # Get decoded, unzipped message body
            m = json.loads(zlib.decompress(b64decode(message.body)))

            # Markdown format the message resources
            r = '```' + json.dumps(m['resources'], indent=4, sort_keys=True) + '```'

            # Compose the Slack message
            slack_message = {
                'channel': os.environ['slack_channel'],
                'attachments': [
                    {
                        "title": "Policy Violation Detected",
                        "fields": [
                            {
                                "title": "Policy",
                                "value": m['policy']['name'],
                                "short": True
                            },
                            {
                                "title": "Account ID :: Region",
                                "value": m['account_id'] + "::" + m['region'],
                                "short": True
                            }
                        ],
                        "color": "#F35A00"
                    },
                    {
                        'title': "Violation",
                        'text': m['action']['violation_desc']
                    },
                    {
                        'title': "Action",
                        'text': m['action']['action_desc']
                    },
                    {
                        'title': 'Resources',
                        'text': r,
                        "mrkdwn_in": ["text"]
                    }
                ]
            }

            r = requests.post(
                os.environ['slack_hook_url'],
                data=json.dumps(slack_message),
                headers={'Content-Type': 'application/json'}
                )
            if r.status_code != 200:
                raise ValueError(
                    'Request to slack returned an error %s, the response is:\n%s'
                    % (response.status_code, response.text)
                )

        message.delete()
