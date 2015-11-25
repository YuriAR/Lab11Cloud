import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import requests

url = "http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key"
data = requests.get(url).text
keys = data.split(":")
access_key_id = keys[0]
secret_access_key = keys[1]

conn = boto.sqs.connect_to_region("eu-west-1",aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

queue = conn.get_queue(sys.argv[1])
messages = queue.get_messages()
if len(messages) > 0:
    print "Message from queue " + sys.argv[1] + ": " + messages[0].get_body()
else:
    print "No messages"
