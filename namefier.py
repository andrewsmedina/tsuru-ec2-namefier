from pymongo import MongoClient
import boto


def ec2_connection():
    return boto.connect_ec2()
