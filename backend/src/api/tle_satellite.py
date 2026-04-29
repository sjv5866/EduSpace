from flask import jsonify
from flask_restful import Resource
from db.db_utils import *
from db.tle import list_tles, get_tle_by_name
from db.pull_tle import convert_tle_to_coords

class TLEList(Resource):
    def get(self):
        return list_tles()
    
class TLE(Resource):
    def get(self, sat_name):
        return get_tle_by_name(sat_name)
    
class TLEPosition(Resource):
    def get(self, sat_name):
        return convert_tle_to_coords(sat_name)

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))