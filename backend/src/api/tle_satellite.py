from flask import jsonify
from flask_restful import Resource
from db.db_utils import *
from db.tle import list_tles, get_tle_by_name
from db.pull_tle import convert_tle_to_coords

class TLEList(Resource):
    def get(self):
        return jsonify(list_tles()), 200
    
class TLE(Resource):
    def get(self, sat_name):
        return jsonify(get_tle_by_name(sat_name)), 200
    
class TLEPosition(Resource):
    def get(self, sat_name):
        return jsonify(convert_tle_to_coords(sat_name)), 200

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))