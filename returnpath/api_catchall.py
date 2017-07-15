from returnpath import api
from flask_restful import Resource
from flask import request
import socket
import logging


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
        return return_obj

api.add_resource(ApiCatchAll, '/', '/<path:path>')
