# save data to json file
import json

# save a list of numbers
numbers = [2, 3, 4, 5, 11, 13]

filename = '../out/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# save a name
username = input("What is your name? ")

filename = '../out/username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll rembember you when you come back, {username}")

# lists and json
bicycles = ['trek', 'specialized', 'cannondale', 'scott']
filename = '../out/bicycles.json'
with open(filename, 'w') as f:
    json.dump(bicycles, f)
    print(f"{bicycles}")
