cars = ['audi', 'toyota', 'lexis', 'bmw', "subaru", 'honda']

# test equality - note case sensitive
for car in cars :
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# test inequality
requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print ('hold the anchovies!')

# multiple conditions
age_0 = 22
age_1 = 44
age_3 = 33

if(age_0 < 21) and (age_1 > 21) :
    print('\nfalse')
else:
    print('\ntrue')

# check if a value is in the list
requested_topping = ['mushrooms', 'sausage', 'extra cheese', 'black olives']
topping = 'mushrooms'

if topping in requested_topping:
    print(f'\n{topping} is one of the requested items')
else:
    print(f"\n{topping} is not one of the requested items")


# check if a value is NOT in the list
banned_users = ['sally', 'bob', 'alice', 'jane']
user = 'marie'

if user not in banned_users:
    print(f"\n{user.title()}, you are allowed to post")


# if-elif-else
age = 13

if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 25
else:
    price = 16

print(f"\nYour admission cost is ${price}")

# to test all conditions, use a series of if statements
print("\nMaking your pizza:")
if 'mushrooms' in requested_topping:
    print ('\tAdding Mushrooms')
if 'black olives' in requested_topping:
    print("\tAdding Black Olives")
if 'anchovies' in requested_topping:
    print("\tAdding Anchovies")

print("\nFinished making your pizza\n")
# 
for topping in requested_topping :
    if topping == 'mushrooms':
        print (f"We're sorry, but we are out of {topping.title()}")
    else:
        print (f"Adding {topping.title()}")

print("\nFinished making your pizza\n")

# check for an empty list
requested_topping = []
if requested_topping:
    for topping in requested_topping:
        print (f"\tAdding {topping.title()}")
else :
    print ('Why are you ordering a plain pizza?')

print("\nFinished making your pizza\n")

# multiple lists
print('\nAdd toppings from available toppings')
requested_toppings = ['mushrooms', 'sausage', 'french fries']
avaliable_toppings = ['pepperoni', 'mushrooms', 'sausage', 'extra cheese', 'black olives']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print (f"Adding {requested_topping.title()}.")
    else :
        print (f"We're sorry but we don't have {requested_topping.title()}")

print("\nFinished making your pizza")
