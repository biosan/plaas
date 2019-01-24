### Build all the Prometheus instruments used in the app
from prometheus_client import Counter, Histogram

requests = Counter('requests', 'Total requests recived')
req_err = Counter('req_err', 'Total requests errors')
plot_lat = Histogram('plot_lat', 'Plotting latency')