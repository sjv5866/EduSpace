from flask import Flask
from flask_restful import Resource, Api
from api.hello_world import HelloWorld
from api.management import *
from db.pull_tle import propagate_tles
from db.db_utils import exec_sql_file
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()
api = Api(app)

api.add_resource(Init, '/manage/init') #Management API for initializing the DB
api.add_resource(Version, '/manage/version') #Management API for checking DB version
api.add_resource(HelloWorld, '/') 


if __name__ == '__main__':
    exec_sql_file('schema/schema.sql')
    propagate_tles()
    scheduler.init_app(app)
    scheduler.add_job(id='daily_tle_propogation', func=propagate_tles, trigger='interval', hours=24)
    scheduler.start()
    app.run(host="0.0.0.0", port=5000)