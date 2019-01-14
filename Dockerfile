FROM czentye/matplotlib-minimal:3.0.2

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY plaas ./plaas
COPY index.html .

EXPOSE 80

CMD ["gunicorn", "-b 0.0.0.0:80", "plaas.app"]