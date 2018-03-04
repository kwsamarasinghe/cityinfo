from flask_restful import Resource
from flask.ext.jsonpify import jsonify

import json

class InfoController(Resource):

    def __init__(self, server):
        self.server = server

    def get(self):
        engine = self.server.getEngine()
        infoResponse = engine.getInfo()
        info = {}
        for response in infoResponse:
            info[response.type] = response.data

        response = {}
        response['version'] = '0.0.1'
        response['data'] = info
        return jsonify(response)
