# dictionaries are key/value pairs
# dictionaries are wrapped in braces {}
# 


# super simple dictionary of an alien color and height
alien_0 = {"color": "green", "height": 36}
print(f"The color of the alien is {alien_0['color']}")
print(f"The height of the alien is {alien_0['height']}")

# add to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# good practice to start out with an empty dictionary and add each element
alien_0 = {}
alien_0['color'] = 'red'
alien_0['height'] = 35
alien_0['x_position'] = 10
alien_0['y_position'] = 75

print(alien_0)

# modify values in the dictionary 
alien_0['color'] = 'yellow'
print(f"The color of the alien is {alien_0['color']}")

#
# Access elements in a dictionary
#
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed']= 'medium'

print(f"\nAlien starting position ({alien_0['x_position']}, {alien_0['y_position']})")

#
# Change values
#

# move the alien to the right
# determine how far to move the alien depending on the speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Alien new position ({alien_0['x_position']}, {alien_0['y_position']})\n")

# del - remove a pair
del alien_0['speed']
print (alien_0)

# example of style
# notice the comma after the last entry - strange it allows this
favorite_languages = {
    'jen': 'javascript',
    'sara' : 'c',
    'ken' : 'go',
    'jack' : 'python',
    'doug' : 'react',
    'edwin' : 'javascript',
}

print(f"\ngroup's favorite languages are {favorite_languages}")
print(f"Jack's favorite language is {favorite_languages['jack'].title()}")

##
# GET
##

# if you try and reference a key that doesn't exist, you get an an error.  
# use get instead

speed = alien_0.get('speed', 'no speed assigned')
print(f"\nSpeed - {speed.title()}")

# items()
#   looping through all items in the dictionary
user_0 = {
    'username' : 'efirmi',
    'first': 'emilio',
    'last': 'firmi',
}
print("\n print key/value of a map")
for key, value in user_0.items() :
    print(f"Key: {key}, Value: {value}")

for name, language in favorite_languages.items() :
    print(f"\n{name.title()}'s favorite language is {language}'")

#
# looping
#

# through all the keys in the dictionary
print("\n loop through favorite language keys")
for name in favorite_languages.keys() :
    print(f"\t{name.title()}")

print("\n Sorted list")
# Sort - Loop through a dictionary's keys in a particular order
for name in sorted(favorite_languages.keys()) :
    print(f"{name.title()}, thank you for taking the poll.")

# loop through all the values
print("\n The following languages have been mentioned:")
for language in favorite_languages.values() :
    print(language.title())

# set - loop through and do not show repetition
print("\n The following languages have been mentioned:")
for language in set(favorite_languages.values()) :
    print(language.title())

#
# Nested Dictionaries
# 

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'blue', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

# list of dictionaries
aliens = [alien_0, alien_1, alien_2]

for alien in aliens :
    print (f"Alien = {alien}")

#
# Range
# 
aliens = []
for alien_number in range(30) :
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change attributes using a slice of 3
for alien in aliens [:3] :
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow' : 
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15



# print the first five
for alien in aliens[:5] :
    print (alien)

print(f"Total number of aliens: {len(aliens)}")

#
# dictionary of lists
#

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print (f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings'] :
    print("\t" + topping)


# save fav languages as a dictionary
favorite_languages = {
    'jen': ['javascript', 'ruby'],
    'sara' : ['c'],
    'ken' : ['go'],
    'jack' : ['python', 'javascript'],
    'doug' : ['react'],
    'edwin' : ['javascript' 'vue'],
}

for name, languages in favorite_languages.items() :
    print (f"\n{name.title()}'s favorite languages are:")
    for language in languages :
        print(f"\t{language.title()}")


# 
# dictionary in a dictionary
# 

users = {
    'aeinstein': {
        'first': 'albert',
        'last' : 'einstein',
        'location': 'princeston',
    },
    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}  

for username, user_info in users.items() :
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"Full name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

