# import just a specific function
# from module_name import function_0, function_1, function_2
from pizza import make_pizza

# import all functions in a module
#   from pizza import *
# 
# maybe dangerous practice with name collisions
# better practice for larger modules is to either
#   import the module and use 'dot' notation
#   or import individual functions



make_pizza('medium', "pepperoni")
make_pizza('large', 'olives', 'mushrooms', 'sausage')


