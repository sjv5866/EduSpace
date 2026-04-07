from flask_restful import Resource
from db import example

class HelloWorld(Resource):
    def get(self):
        return "<p>Hello, World!</p>"