import falcon, logging

logger = logging.getLogger(__name__)

class Index(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()
        logger.debug('Served index page')