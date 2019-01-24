FROM czentye/matplotlib-minimal:3.0.2

WORKDIR /app

# Add fonts (Humor-Sans) and update fonts cache
# then delete fontconfig (isn't necessary anymore) and clean cache
COPY fonts /root/.fonts
RUN apk --update add fontconfig && \
    fc-cache -fv && \
    apk del --purge fontconfig && \
    rm -vrf /var/cache/apk/*

# Add requirements file
COPY requirements.txt .
# Install requirements
RUN pip install -r requirements.txt

# Add source code
COPY plaas ./plaas
COPY logging.conf .
COPY index.html .
COPY gunicorn.py .

# The prometheus_multiproc_dir environment variable must be set to a directory that the client library can use for metrics.
# See: https://github.com/prometheus/client_python
RUN mkdir ./multiproc-tmp
ENV prometheus_multiproc_dir=./multiproc-tmp

# Expose port and run the app
EXPOSE ${PORT:-80}
CMD gunicorn -b 0.0.0.0:${PORT:-80} -c gunicorn.py plaas.app