import json, logging

import falcon

from .functions import plot_it
from .instruments import requests, req_err


logger = logging.getLogger(__name__)

class Plot(object):

    def on_get(self, req, resp):


        # Validate data
        # TODO: Finer error logging and handling,
        #       differentiate between title or data errors
        #       and invalid or missing parameter.
        try:
            title = req.params['title']
            data  = req.params['data']
            data  = tuple(map(float, data))
        except ValueError:
            # TODO: Better error logging message
            # Error logs and metrics
            req_err.inc()
            logger.exception('Invalid query string')
            raise falcon.HTTPInvalidParam('Invalid query string',
                                          'title or data')
        
        # Logs and metrics
        logger.debug("Received new request")
        requests.inc()

        # Send image as response
        resp.data = plot_it(title, data)
        resp.content_type = falcon.MEDIA_PNG
        resp.status = falcon.HTTP_200