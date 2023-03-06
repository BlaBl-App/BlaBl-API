from api.manage_db import init_db


def on_starting(server):
    init_db()
