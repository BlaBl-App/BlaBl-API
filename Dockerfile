FROM python:3-slim

ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt

# run flask app
CMD ["python", "app.py"]