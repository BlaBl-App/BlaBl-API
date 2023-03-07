import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from .common import add_forum_into_file, get_forums_from_file, remove_forum
from .manage_db import init_db, insert_message, select_last_message_id, select_message

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return "Hey 👋 it's working! <br>This is the root of BlaBl'App API please read the <a href='https://github.com/BlaBl-App/BlaBl-API'>instruction</a>"


@app.route("/api", methods=["GET"])
def get_serv_info():
    return jsonify({"success": True, "name": "mother API"})


@app.route("/api/forums", methods=["GET"])
def get_forums():
    # returns a list of forums object {"id": int, "name": str, "description": str}
    return jsonify({"success": True, "forums": get_forums_from_file()})


@app.route("/api/forums", methods=["POST"])
def add_forum():
    name = request.form.get("name", default="")
    description = request.form.get("description", default="")

    logging.info(f"name={name} description={description}")

    # name is mandatory
    if name == "":
        return jsonify({"success": False})
    success = add_forum_into_file(name, description)
    return jsonify({"success": success})


@app.route("/api/forums", methods=["DELETE"])
def delete_forum():
    id = request.form.get("id", default=-1)
    id = int(id)
    logging.info(f"id={id}")
    # id is mandatory
    if id == -1:
        return jsonify({"success": False})
    success = remove_forum(id)
    return jsonify({"success": success})


@app.route("/api/message", methods=["GET"])
def get_messsage():
    nb_message = request.args.get("nb", default=10)
    start = request.args.get("start", default=0)
    forum = request.args.get("forum", default=1)

    logging.info(f"nb_message={nb_message} start={start} forum={forum}")

    return jsonify(
        {"success": True, "messages": select_message(nb_message, start, forum)}
    )


@app.route("/api/message", methods=["POST"])
def post_message():
    nickname = request.form.get("nickname", default=None)
    pic = request.form.get("pic", default="")
    message = request.form.get("message", default="")
    forum = request.form.get("forum", default=1)

    logging.info(f"nickname={nickname} pic={pic} message={message} forum={forum}")

    # nickname is mandatory
    if nickname == "":
        return jsonify({"success": False})
    success = insert_message(nickname, pic, message, forum)
    return jsonify({"success": success})


@app.route("/api/last_message_id", methods=["GET"])
def get_last_message_id():
    forum = request.args.get("forum", default=1)

    last_message_id = select_last_message_id(forum)

    logging.info(f"last_message_id={last_message_id}")

    return jsonify({"success": "true", "last_message_id": last_message_id})


def main():
    init_db()
    app.run(host="0.0.0.0", port=5555)
