import logging

from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route("/")
def root():
    return "Hey 👋 it's working! <br>This is the root of BlaBl'App API please read the <a href='https://github.com/BlaBl-App/BlaBl-API'>instruction</a>"


@app.route("/api/message", methods=["GET"])
def get_messsage():
    nb_message = request.form.get("nb", default="")
    start = request.form.get("start", default="")

    return jsonify(
        {
            "sucess": "true",
            "messages": [
                {"id": 12, "nickname": "bob", "pick": "", "message": "hello"},
                {"id": 12, "nickname": "alice", "pick": "", "message": "hi"},
                {
                    "id": 12,
                    "nickname": "alice",
                    "pick": "",
                    "message": "nice to meet you Alice",
                },
                {
                    "id": 12,
                    "nickname": "bob",
                    "pick": "",
                    "message": "where are you from",
                },
            ],
        }
    )


@app.route("/api/message", methods=["POST"])
def post_messsage():
    nickname = request.form.get("nickname", default="")
    pick = request.form.get("pick", default="")
    message = request.form.get("message", default="")

    logging.info(f"nickname={nickname} pick={pick} message={message}")

    # nickname is mandatory
    if nickname == "":
        return jsonify({"sucess": "false"})
    else:
        return jsonify({"sucess": "true"})
