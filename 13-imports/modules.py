#####
# Notes on importing modules and functions
#
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# from module_name import function_name
# import module_name as mn
# from module_name import * 
#####

# import an entire module
import pizza

# I can also use an alias for the module
# import pizza as as p

pizza.make_pizza('medium', "pepperoni")
pizza.make_pizza('large', 'olives', 'sausage', 'mushrooms')


# using the alias
# p.make_pizza(...)

