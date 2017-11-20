venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

package: venv
	cp awslambda.py venv/lib/python2.7/site-packages/
	cd 	venv/lib/python2.7/site-packages/ && \
		zip -9 -r /tmp/sqs2slack.zip * -x \*.rst
	shasum -a 256 -p /tmp/sqs2slack.zip > /tmp/sqs2slack.sha

clean:
	rm -rf venv /tmp/sqs2slack.*
