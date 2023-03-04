import json


def get_forums_from_file():
    with open("forums.json", "r") as f:
        return json.load(f).get("forums")
    

if __name__ == "__main__":
    print(get_forums_from_file())