from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.db_utils import *

from db.tle import listTLES

class Init(Resource):
    def get(self):
        return listTLES()

class Version(Resource):
    def get(self):
        return (exec_get_one('SELECT VERSION()'))