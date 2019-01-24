# Required for using Prometheus with Gunicorn
# See: https://github.com/prometheus/client_python
from prometheus_client import multiprocess

def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)