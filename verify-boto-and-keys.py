import requests
import boto

url = "http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key"
data = requests.get(url).text
keys = data.split(":")
accessKey = keys[0]
secretKey = keys[1]
print "Boto Version: " + boto.Version
print "Access key: " + accessKey
print "Secret key: " + secretKey
