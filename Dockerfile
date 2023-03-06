FROM python:3-slim

ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt

# run flask app
EXPOSE 5555
CMD ["gunicorn", "-b", "0.0.0.0:5555", "-k", "gevent", "-w", "4","--preload", "-c", "conf.py" ,  "api.app:app"]
