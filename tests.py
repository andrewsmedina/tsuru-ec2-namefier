import unittest
import mock

from namefier import ec2_connection


class Ec2Test(unittest.TestCase):
    @mock.patch("boto.connect_ec2")
    def test_ec2_connection(self, conn):
        ec2_connection()
        conn.assert_called_with()


unittest.main()
