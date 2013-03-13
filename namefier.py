import pymongo
import boto


def ec2_connection():
    return boto.connect_ec2()


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
