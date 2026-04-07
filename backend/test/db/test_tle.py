import unittest
from src.db.tle import *
from src.db.db_utils import *

class TestTLE(unittest.TestCase):

    def test_build_tables(self):
        """Build the tables"""
        buildTable()
        result = exec_get_all('SELECT * FROM tles')
        self.assertEqual([], result, "no rows in tles")