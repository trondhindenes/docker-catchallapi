import json
import logging
import os
import socket

from flask import request
from flask_restful import Resource

from returnpath import api

logger = logging.getLogger('returnpath')

SHOW_ENVVARS = os.getenv('SHOW_ENVVARS', 'false').lower() == 'true'


def get_envvars():
    env_vars = {}
    for name, value in os.environ.items():
        env_vars[name] = value
    return env_vars


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
        if SHOW_ENVVARS:
            return_obj['env'] = get_envvars()

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
        if SHOW_ENVVARS:
            return_obj['env'] = get_envvars()
        print(json.dumps(return_obj, indent=4, sort_keys=True))
        return return_obj


api.add_resource(ApiCatchAll, '/', '/<path:path>')
