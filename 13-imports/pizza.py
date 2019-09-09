# pass arbitrary numbers of arguments
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"Making a {size} pizza with the following toppings")
    # print(toppings)
    # use a for loop instead
    for topping in toppings:
        print(f" - {topping}")
