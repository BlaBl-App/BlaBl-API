import logging

from flask import Flask, jsonify, request

from .common import add_forum, get_forums_from_file, remove_forum
from .manage_db import init_db, insert_message, select_message

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route("/")
def root():
    return "Hey 👋 it's working! <br>This is the root of BlaBl'App API please read the <a href='https://github.com/BlaBl-App/BlaBl-API'>instruction</a>"


@app.route("/api/forums", methods=["GET"])
def get_forums():
    # returns a list of forums object {"id": int, "name": str, "description": str}
    return jsonify({"success": "true", "forums": get_forums_from_file()})


@app.route("/api/forums", methods=["POST"])
def add_forum():
    name = request.form.get("name", default="")
    description = request.form.get("description", default="")

    logging.info(f"name={name} description={description}")

    # name is mandatory
    if name == "":
        return jsonify({"success": "false"})
    success = add_forum(name, description)
    return jsonify({"success": success})


@app.route("/api/forums", methods=["DELETE"])
def delete_forum():
    id = request.form.get("id", default=-1)
    logging.info(f"id={id}")

    # id is mandatory
    if id == -1:
        return jsonify({"success": "false"})
    success = remove_forum(id)
    return jsonify({"success": success})


@app.route("/api/message", methods=["GET"])
def get_messsage():
    nb_message = request.form.get("nb", default=10)
    start = request.form.get("start", default=0)
    forum = request.form.get("forum", default=1)

    logging.info(f"nb_message={nb_message} start={start} forum={forum}")

    return jsonify({"success": "true", "messages": select_message(nb_message, start, forum)})


@app.route("/api/message", methods=["POST"])
def post_message():
    nickname = request.form.get("nickname", default="")
    pic = request.form.get("pic", default="")
    message = request.form.get("message", default="")
    forum = request.form.get("forum", default="")

    logging.info(f"nickname={nickname} pic={pic} message={message} forum={forum}")

    # nickname is mandatory
    if nickname == "":
        return jsonify({"success": "false"})
    success = insert_message(nickname, pic, message)
    return jsonify({"sucess": success})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5555)
