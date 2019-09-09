# using 'as' to give make_pizza an alias
# good when there might be a naming conflict
from pizza import make_pizza as mp 

mp('medium', 'cheese')
mp('large', 'anchovies', 'cheese', 'pepperoni')




