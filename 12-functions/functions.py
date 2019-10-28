# 
# Simple function
#

# def - define a function
def greet_users(username) :
    # doc string - what the function does - triple quotes
    """Define a simple greeting."""
    print(f"hello {username.title()}")

# 
# arguments
#
def describe_pet(pet_name, animal_type = 'dog') :
    """describe information about a pet"""
    print(f"\nI have a pet of type {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#
# type hints - float here is a hint, not enforced at runtime.
#
def double(number: float) -> float:
    return 2 * number

#
# Return arguments
#
def get_formatted_name(first_name, last_name) :
    """Return a full name, neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#
# optional parameters - set to an empty string
#
def get_full_name(first_name, last_name, middle_name = '') :
    """Return a full name, neatly formatted """
    if middle_name :
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

#
# return a dictionary
#
def build_person(first_name, last_name, age=None) :
    ### return dictionary about a person ###
    person = {'first':first_name, 'last':last_name}
    if (age) :
        person['age'] = age
    return person

#
# modify lists in a function
#
def print_models(unprinted_designs, completed_models) :
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    print(f"print_models --> {len(unprinted_designs)}")
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_models in completed_models:
        print(completed_models)

# pass arbitrary numbers of arguments
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"Making a {size} pizza with the following toppings")
    # print(toppings)
    # use a for loop instead
    for topping in toppings:
        print(f" - {topping}")

# pass arbitrary keyword arguments
def build_profile(first, last, **user_info) :
    """build a dictionary about everything we need to know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

######################

# type hint, not enforced
print(double(3.3))
print(double("I am not a float"))

greet_users("jesse")

# positional arguments functions
describe_pet("harry", "hamster")
describe_pet("fido", "dog")

# keyword arguments - free you up from having the order correct
describe_pet(animal_type = "cat", pet_name = "felix")

# default argument
describe_pet("jojo")

# equivelant calls - same results
describe_pet('willie')
describe_pet(pet_name = 'willie')
describe_pet( animal_type='dog', pet_name = 'willie')

# return values
musician = get_formatted_name("jimmy", "hendrix")
print (f"\n{musician}")

# default parameters
musician = get_full_name(first_name = "stevie", middle_name="ray", last_name = "vaughn")
print (f"\n{musician}")
musician = get_full_name("Jimmy", "hendricks")
print (f"\n{musician}")

# return a dictionary
musician = build_person("Glen", "Fry")
print (f"\n{musician}")
musician = build_person("jimmy", "hendrix", 27)
print (f"\n{musician}")


# while loop calling a function
while True :
    print ("\nPlease tell me your name")
    print ("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q' :
        break

    l_name = input("Last Name: ")
    if l_name == 'q' :
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name.title()}")

# modify lists in functions
unprinted_designs = ['phone case', 'robot penant', 'dodeahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# read-only copy of list - send slice notation
unprinted_designs = ['phone case', 'robot penant', 'dodeahedron']
print(f"sending copy of the list... {len(unprinted_designs)}")
print_models(unprinted_designs[:], completed_models)

# pass arbitrary numbers of arguments
make_pizza('medium', 'peperonni')
make_pizza('large', 'mushrooms', 'olives', 'sausage', 'extra-cheese')

# arbitrary keyword arguments
user_profile = build_profile('albert', 'einstein', 
        location='princeston',
        field='physics')

print(user_profile)

