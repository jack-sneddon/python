# copy list using the ":"
my_food = ["pizza", "salad", "bbq", "falafel"]
friends_food = my_food[:]

print('my favorite foods are: ')
print(my_food)

print("\nmy friend's favorite food")
print(friends_food)

my_food.append('mole')
friends_food.append('broccoli')

print('\nmy favorite foods are: ')
print(my_food)

print("\nmy friend's favorite food")
print(friends_food)

# if I assign the lists, it will just point to the same list
# friends_food = my_food
# my_food.append('ice cream')
# print(friend_food)

