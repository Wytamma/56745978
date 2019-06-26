from flask_restplus import Api
from flask import Blueprint
from .main.controller.hello_controller import api as hello

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='My RESTful API',
          version='1.0',
          description='My flask restplus web service'
          )

api.add_namespace(hello, path='/hello')