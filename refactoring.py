from pathlib import Path
import json

def get_stored_username(path):
    if path.exist():
        contents = path.read_text()
        username = contents.load_text()
        return username
    else:
        return None
def get_new_username(path):
    username = input('what is your username')
    contents = json.dumps()
    path.write_text(contents)
    return username
def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
greet_user()