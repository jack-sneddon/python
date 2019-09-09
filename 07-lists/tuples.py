# tuples are an immutable list
# use parenthasis instead of brackets

dimentions = (200, 50)
print(dimentions[0])
print(dimentions[1])

# error
# dimentions[0] = 250  

# print all dimentions
print(dimentions)

# we can replace a tuple
dimentions = (400,75)
print(dimentions)

# menu items
print("\n Dessert Menu: ")
dessert_menu = ("cake", "icecream", "canolie", "cupcake", "lemon bars" )
for item in dessert_menu:
    print(item)

#only way to remove canolie is to replace the tuple
print("\n Dessert Menu: ")
dessert_menu = ("cake", "icecream", "cupcake", "lemon bars" )
for item in dessert_menu:
    print(item)
