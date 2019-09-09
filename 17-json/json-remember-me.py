import json

def get_stored_username ():
    """Get stored user if available"""
    filename = '../out/username.json'
    try:
        with open(filename) as f:
           username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username () :
    """prompt for new username"""
    username = input("What is your name? ")
    filename = '../out/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """
    Greet user by name.
    Load the username, if it has been stored previously.
    Otherwise, prompt for the username and store it.
    """
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:        
        username = get_new_username()
        print(f"We'll rembember you when you come back, {username}")
        
greet_user()