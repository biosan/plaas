### Prometheus '/metrics' endpoint
from prometheus_client import multiprocess, CollectorRegistry, generate_latest

class PrometheusResource(object):

    def on_get(self, req, resp):
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        data = generate_latest(registry)
        resp.data = data
        resp.content_type = 'CONTENT_TYPE_LATEST'