import unittest
import mock

from namefier import ec2_connection, mongo_connection, namefy


class Ec2Test(unittest.TestCase):
    @mock.patch("boto.connect_ec2")
    def test_ec2_connection(self, conn):
        ec2_connection()
        conn.assert_called_with()


class MongoTest(unittest.TestCase):
    @mock.patch("pymongo.MongoClient")
    def test_mongo_connection(self, conn):
        mongo_connection()


class NamefyTest(unittest.TestCase):
    @mock.patch("boto.connect_ec2")
    def test_namefy(self, ec2):
        conn = ec2.return_value
        apps = [{
            "units": [
                {"name": "vm1", "instanceid": "i-1"}
            ]
        }]
        namefy(apps)
        conn.create_tags.assert_called_with(["i-1"], {"Name": "vm1"})


unittest.main()
