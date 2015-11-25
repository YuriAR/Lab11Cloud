import sys
import boto.sqs
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import requests

url = "http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key"
data = requests.get(url).text
keys = data.split(":")
access_key_id = keys[0]
secret_access_key = keys[1]

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

#Create a queue
name = "D15124347-" + sys.argv[1]
queue = conn.create_queue(name)
print "Queue " + name + " created"
