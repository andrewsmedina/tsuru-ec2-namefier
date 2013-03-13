import pymongo
import boto


def ec2_connection():
    return boto.connect_ec2()


def mongo_connection():
    return pymongo.MongoClient('localhost', 27017)
