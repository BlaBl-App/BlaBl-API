from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/messsage',methods = ['GET'])
def get_messsage():
    return 'GET messsage'

@app.route('/api/messsage',methods = ['POST'])
def post_messsage():
    return 'POST messsage'+ request.data
