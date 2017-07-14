from returnpath import api
from flask_restful import Resource
import logging


logger = logging.getLogger('returnpath')

class ApiCatchAll(Resource):
    def get(self, path=None):
        if path is None:
            path = '/'

        if path.startswith('/'):
            pass
        else:
            path = '/' + path
        return path

api.add_resource(ApiCatchAll, '/', '/<path:path>')
