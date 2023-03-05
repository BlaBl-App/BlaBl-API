import json


def get_forums_from_file():
    with open("forums.json", "r") as f:
        return json.load(f).get("forums")
    

def add_forum(name, description):
    with open("forums.json", "r") as f:
        data = json.load(f)
        data["forums"].append({"id": get_last_id_forum(), "name": name, "description": description})
    with open("forums.json", "w") as f:
        json.dump(data, f)
    return True


def remove_forum(id):
    with open("forums.json", "r") as f:
        data = json.load(f)
        data["forums"] = [forum for forum in data["forums"] if forum["id"] != id]
    with open("forums.json", "w") as f:
        json.dump(data, f)
    return True


def get_last_id_forum():
    with open("forums.json", "r") as f:
        data = json.load(f)
        return len(data["forums"]) + 1
    