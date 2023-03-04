import logging

from flask import Flask, jsonify, request

from manage_db import init_db, insert_message, select_message

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route("/")
def root():
    return "Hey 👋 it's working! <br>This is the root of BlaBl'App API please read the <a href='https://github.com/BlaBl-App/BlaBl-API'>instruction</a>"


@app.route("/api/message", methods=["GET"])
def get_messsage():
    nb_message = request.form.get("nb", default=None)
    start = request.form.get("start", default=None)

    if nb_message is None and start is None:
        return jsonify({"success": "false", "messages": select_message()})
    elif nb_message is None:
        return jsonify({"success": "false", "messages": select_message(start=start)})
    elif start is None:
        return jsonify({"success": "false", "messages": select_message(nb_message=nb_message)})
    return jsonify({"success": "true", "messages": select_message(nb_message, start)})


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
