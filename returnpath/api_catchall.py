from returnpath import api
from flask_restful import Resource
from flask import request
import logging


logger = logging.getLogger('returnpath')

class ApiCatchAll(Resource):
    def get(self, path=None):
        if path is None:
            path = '/'

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
            'headers': out_headers
        }
        return return_obj

api.add_resource(ApiCatchAll, '/', '/<path:path>')
