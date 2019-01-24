import falcon

### Logging setup
import logging, logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()
# Hacky way to set logging level from environ variable. default: INFO
from os import environ
logger.setLevel(logging._nameToLevel.get(environ.get("LOG_LEVEL", "INFO"), "INFO"))

# Import endpoint resources
from .plot import Plot
from .prometheus import PrometheusResource

# Create API
api = application = falcon.API()

# Create endpoints resources
plot = Plot()
metrics = PrometheusResource()

# TODO: How to manage dev/prod configuartion differences?
local = True
if local == True:
    from .index import Index
    api.add_route('/', Index())

# Add routes to resources
api.add_route('/plot', plot)
api.add_route('/metrics', metrics)