import unittest
from src.db.tle import *
from src.db.db_utils import *

class TestTLE(unittest.TestCase):

    def test_build_tables(self):
        """Build the tables"""
        result = exec_get_all('SELECT * FROM tles')
        self.assertEqual(28, len(result), "no rows in tles")

    def test_get_tle_by_name(self):
        "grab specific TLE from database"
        result = get_tle_by_name("TEST")
        self.assertEqual('TEST', result.satellite_name, 'cannot pull satellite name')
        self.assertEqual('LINE 1', result.line1, 'cannot pull line1 from TLE')
        self.assertEqual('LINE 2', result.line2, 'cannot pull line2 from TLE')
        self.assertEqual('TEST', result.source, 'cannot pull source')