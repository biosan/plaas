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

# Expose port and run the app
EXPOSE 80
CMD ["gunicorn", "-b 0.0.0.0:80", "plaas.app"]