import json
from flask import request
from flask_restplus import Resource, Namespace

api = Namespace('hello', description='hello world')


@api.route('/', methods=['GET'])
class Hello(Resource):
    @api.param('name1', 'Name1')
    @api.param('name2', 'Name2')
    def get(self):
        """ Get Hello names """
        return "Hello", 200