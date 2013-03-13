from boto import ec2
import pymongo
import os


def ec2_connection():
    region = os.environ.get("AWS_REGION", "sa-east-1")
    access = os.environ.get("AWS_ACCESS_KEY_ID", "")
    secret = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
    return ec2.connect_to_region(region,
                                 aws_access_key_id=access,
                                 aws_secret_access_key=secret)


def mongo_connection():
    return pymongo.MongoClient('localhost', 27017)


def namefy(apps):
    ec2 = ec2_connection()
    tags = [tag.value for tag in ec2.get_all_tags() if tag.name == "Name"]
    for app in apps:
        for unit in app["units"]:
            if unit["name"] not in tags:
                ec2.create_tags([unit["instanceid"]], {"Name": unit["name"]})


def main():
    apps = mongo_connection().tsuru.apps.find()
    namefy(apps)


if __name__ == "__main__":
    main()
