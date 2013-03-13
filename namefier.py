import pymongo
import boto


def ec2_connection():
    return boto.connect_ec2()


def mongo_connection():
    return pymongo.MongoClient('localhost', 27017)


def namefier(apps):
    ec2 = ec2_connection()
    for app in apps:
        for unit in app["units"]:
            ec2.create_tags([unit["instanceid"]], {"name": unit["name"]})


def main():
    apps = mongo_connection().tsuru.apps.find()
    namefier(apps)


if __name__ == "__main__":
    main()
