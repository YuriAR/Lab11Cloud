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

#Delete
queue = conn.get_queue(sys.argv[1])
conn.delete_queue(queue)
print "Queue deleted " + sys.argv[1]
