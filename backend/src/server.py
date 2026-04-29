from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from api.tle_satellite import *
from db.pull_tle import propagate_tles
from db.db_utils import exec_sql_file
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()
api = Api(app)
CORS(app)

api.add_resource(TLEList, '/tles') # Grab list of all TLE data from database
api.add_resource(TLE, '/tles/<sat_name>') # Grabs unique TLE data of target satellite from database
api.add_resource(TLEPosition, '/tles/pos/<sat_name>') # Location data from specific TLE
api.add_resource(Version, '/version') #Management API for checking DB version

if __name__ == '__main__':
    exec_sql_file('schema/schema.sql')
    propagate_tles()
    scheduler.init_app(app)
    scheduler.add_job(id='daily_tle_propogation', func=propagate_tles, trigger='interval', hours=24)
    scheduler.start()
    app.run(host="0.0.0.0", port=5000)