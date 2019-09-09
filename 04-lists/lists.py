# square brackets ([]) indicate a list
# individual elements are seperated by commas

bicycles = ['trek', 'specialized', 'cannondale', 'scott']

print (bicycles)

print(bicycles[0])
print(bicycles[0].title())

# last element in the list - use "-1"
print (bicycles[-1])

# pull an element from a list
message = f"My first bycicle was a {bicycles[0].title()}."
print (message)

# append - add elements to the end of the list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('bmw')
motorcycles.append('indian')
print (motorcycles)

# change an element 
motorcycles[0] = 'ducati'
print (motorcycles)

# insert an element at a specific location
motorcycles.insert(0, 'yamaha')
print(motorcycles)

# keyword 'del' deletes an element from the list
del motorcycles[2]
print(motorcycles)

# pop a value out of the list
last_owned_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"The last owned motorcycle was {last_owned_motorcycle.title()}.")

first_owned_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"The first owned motorcycle was {first_owned_motorcycle.title()}.")

# pop at a specific location
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"\nMy first owned motorcycle was {first_owned.title()}.")

# Remove an item by value
motorcycles = ['ducati', 'honda', 'suzuki', 'indian']
print (motorcycles)
motorcycles.remove('suzuki')
print (motorcycles)

# Remove an item, but also include a reason
# note, this only removes the first one in the list
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print (f"\nA {too_expensive.title()} is too expensive for me.")



