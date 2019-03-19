from returnpath import api
from flask_restful import Resource
from flask import request
import socket
import logging
import json


logger = logging.getLogger('returnpath')

class ApiCatchAll(Resource):
    def get(self, path=None):
        if path is None:
            path = '/'

        node_name = socket.gethostname()

        out_headers = {}
        headers = request.headers.environ
        for header in headers.keys():
            if header.startswith('wsgi'):
                pass
            elif header.startswith('werkzeug'):
                pass
            else:
                out_headers[header] = headers[header]


        if path.startswith('/'):
            pass
        else:
            path = '/' + path

        return_obj = {
            'path': path,
            'headers': out_headers,
            'local_computer_name': node_name
        }
        print(json.dumps(return_obj, indent=4, sort_keys=True))
        return return_obj

    def post(self, path=None):
        if path is None:
            path = '/'

        node_name = socket.gethostname()

        out_headers = {}
        headers = request.headers.environ

        for header in headers.keys():
            if header.startswith('wsgi'):
                pass
            elif header.startswith('werkzeug'):
                pass
            else:
                out_headers[header] = headers[header]

        try:
            request_json = request.json
        except:
            request_json = None

        try:
            request_values = request.values
        except:
            request_values = None

        if path.startswith('/'):
            pass
        else:
            path = '/' + path

        return_obj = {
            'path': path,
            'headers': out_headers,
            'local_computer_name': node_name,
            'request': {
                'json_body': request_json,
                'values': request_values
            }
        }
        print(json.dumps(return_obj, indent=4, sort_keys=True))
        return return_obj

api.add_resource(ApiCatchAll, '/', '/<path:path>')
