import json

filename = '../out/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

# remember a name
filename = '../out/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}")

# read a list
filename = '../out/bicycles.json'
with open(filename) as f:
    bicycles = json.load(f)
    print(bicycles)