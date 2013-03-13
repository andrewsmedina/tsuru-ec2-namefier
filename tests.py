import unittest
import mock

from namefier import ec2_connection, mongo_connection


class Ec2Test(unittest.TestCase):
    @mock.patch("boto.connect_ec2")
    def test_ec2_connection(self, conn):
        ec2_connection()
        conn.assert_called_with()


class MongoTest(unittest.TestCase):
    @mock.patch("pymongo.MongoClient")
    def test_mongo_connection(self, conn):
        mongo_connection()

unittest.main()
