# a for loop is effective for looping through a list, but you shouldn't modify a 
# list inside for loop because Pything will have trouble keeping track of the items
# in the list.  To modify a list as you work throuh it, use a while loop.  
# Using while loops with lists and dictionaries allows you to collect, store, and 
# organize lots of input to examine and report on later.

# 
# move items from one list to another
#

# start with populated list and an empty list 
unconfirmed_users = ['alice', 'bob', 'candice']
confirmed_users = []

# verfiy each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print(f"Verifying user: {confirmed_user.title()}")
    confirmed_users.append(confirmed_user)


# remove all instances of a specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"\npets = {pets}")

# use the 'remove' command only removes the first instance
pets.remove('cat')
print(f"\npets = {pets}")

# use while loop
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets :
    pets.remove('cat')
print(f"\npets = {pets}")

#
# Fill out a dictionary
# 

responses = {}

# Set active flag to indicate that polling is active
polling_active = True

while polling_active :
    # prompt for the pserson's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response 

    # find out if anyone else is going to take the poll.
    repeat = input ("Would you like to let another person respond (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling complete, Show results
print("\n --- Polling Results ---")
for name, response in responses.items() :
    print(f"{name.title()} would like to climb {response.title()}")






