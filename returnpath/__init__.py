from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from returnpath.config_helper import ConfigHelper
import sys
import returnpath.log

this_path = sys.path[0]

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

#config = ConfigHelper.get_config_path('config.yml')

#appconfig = {}
#appconfig['logging_level'] = ConfigHelper.get_config_variable(config, 'logging_level', format='yaml')
#logger = log.setup_custom_logger(appconfig['logging_level'])
logger = log.setup_custom_logger('info')

app.config['BUNDLE_ERRORS'] = True
api = Api(app)
from returnpath.api_catchall import ApiCatchAll

