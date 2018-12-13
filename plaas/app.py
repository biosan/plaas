import falcon

import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

from .plot import Plot


api = application = falcon.API()

plot = Plot()

# TODO: How to manage dev/prod configuartion differences?
local = True
if local == True:
    from .index import Index
    api.add_route('/', Index())

api.add_route('/plot', plot)