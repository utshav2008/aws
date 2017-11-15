#!/usr/bin/python
'''
    File name: s3file.py 
    Author: Utshav Singh
    Date created: 15/11/2017
    Date last modified: 15/11/2017
    Python Version: 2.7
'''

import boto
from boto.s3.key import Key

keyId = "<ur access keys>"
sKeyId= "<ur secret keys>"
conn = boto.connect_s3(keyId,sKeyId)      #Connect to S3

def listbuckets():
	buckets = conn.get_all_buckets()          #Get the bucket list
	for i in buckets:
    		print(i.name)

def listfiles(bucketname):
	bucket = conn.get_bucket(bucketname)   #Get the files in the bucket
	for o in bucket.list(delimiter='/'):
    		print(o.name)

def getfile(bucketname,sourcefile,destinationfile):
	srcFileName=sourcefile
	destFileName=destinationfile
	bucketName=bucketname
	bucket = conn.get_bucket(bucketName)
	#Get the Key object of the given key, in the bucket
	k = Key(bucket,srcFileName)
	#Get the contents of the key into a file 
	k.get_contents_to_filename(destFileName)

def main():
	listbuckets()
	bucketname = raw_input("Which bucket you want to list? ")
	listfiles(bucketname)
	sourcefile = raw_input("which file to get from above bucket? ")
	destinationfile = raw_input("Destination file where the content will be copied? ")
	getfile(bucketname,sourcefile,destinationfile)	

if __name__ == "__main__":
	main()


