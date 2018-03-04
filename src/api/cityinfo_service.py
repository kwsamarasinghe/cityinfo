from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify

from info_controller import InfoController as infoController

class CityInfoService:

    def __init__(self, server):
        self.server = server

        #Flask app
        self.app = Flask(__name__)
        self.api = Api(self.app)

        #Adds the info resource
        self.api.add_resource(infoController, '/getinfo',
            resource_class_kwargs={'server' : self.server})


    def start(self):
        port = int(self.server.serverPort)
        self.app.run(port=port)
