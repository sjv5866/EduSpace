import unittest
from src.db.tle import *
from src.db.db_utils import *

class TestTLE(unittest.TestCase):

    def test_build_tables(self):
        """Build the tables"""
        result = exec_get_all('SELECT * FROM tles')
        self.assertEqual(28, len(result), "no rows in tles")

    def test_list_tles(self):
        """grab a list of all tles in database"""
        result = list_tles()
        self.assertTrue(len(result) > 0, "failed to fetch tles from database")

    def test_get_tle_by_name(self):
        """grab specific TLE from database"""
        result = get_tle_by_name("TEST")
        self.assertEqual(1, result.satellite_id, 'cannot pull satellite id')
        self.assertEqual('TEST', result.satellite_name, 'cannot pull satellite name')
        self.assertEqual('LINE 1', result.line1, 'cannot pull line1 from TLE')
        self.assertEqual('LINE 2', result.line2, 'cannot pull line2 from TLE')
        self.assertEqual('TEST', result.source, 'cannot pull source')

    def test_insert_tle(self):
        """test insert into database"""
        mock_tle = {
            "sat_id": 1776,
            "sat_name": "TEST",
            "line_1": "line_1",
            "line_2": "line_2",
            "source": 'CelesTrak'
        }

        insert_tle(mock_tle)
        result = get_tle_by_name("TEST")
        self.assertEqual(mock_tle.sat_id, result.satellite_id, 'failed to update satellite id')
        self.assertEqual('TEST', result.satellite_name, 'failed to update satellite name')
        self.assertEqual(mock_tle.line_1, result.line1, 'failed to update line1 from TLE')
        self.assertEqual(mock_tle.line_2, result.line2, 'failed to update line2 from TLE')
        self.assertEqual('TEST', result.source, 'failed to update source')
