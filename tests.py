import unittest
import mock

from namefier import ec2_connection, mongo_connection, namefy


class Ec2Test(unittest.TestCase):
    @mock.patch("boto.ec2.connect_to_region")
    def test_ec2_connection(self, conn):
        ec2_connection()
        conn.assert_called_with('sa-east-1',
                                aws_access_key_id='',
                                aws_secret_access_key='')


class MongoTest(unittest.TestCase):
    @mock.patch("pymongo.MongoClient")
    def test_mongo_connection(self, conn):
        mongo_connection()


class NamefyTest(unittest.TestCase):
    @mock.patch("boto.ec2.connect_to_region")
    def test_namefy(self, ec2):
        conn = ec2.return_value
        apps = [{
            "units": [
                {"name": "vm1", "instanceid": "i-1"}
            ]
        }]
        namefy(apps)
        conn.create_tags.assert_called_with(["i-1"], {"Name": "vm1"})

    @mock.patch("boto.ec2.connect_to_region")
    def test_namefy_when_tag_already_exisits(self, ec2):
        class Tag(object):
            name = "Name"
            value = "vm1"

        conn = ec2.return_value
        conn.get_all_tags.return_value = [Tag()]
        apps = [{
            "units": [
                {"name": "vm1", "instanceid": "i-1"},
                {"name": "vm2", "instanceid": "i-2"},
            ]
        }]
        namefy(apps)
        conn.create_tags.assert_called_once_with(["i-2"], {"Name": "vm2"})


unittest.main()
