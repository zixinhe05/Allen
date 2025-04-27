from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():  # Corrected method
        with open(path, 'r') as file:  # Opening the file for reading
            contents = json.load(file)  # Correct way to parse JSON
            return contents.get('username')  # Return the username stored in the dictionary
    else:
        return None

def get_new_username(path):
    username = input('What is your username? ')
    contents = {'username': username}  # Create a dictionary with the username
    with open(path, 'w') as file:  # Open the file for writing
        json.dump(contents, file)  # Write the dictionary to the file in JSON format
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
