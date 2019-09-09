# numerical lists
print ("\n***Numerical Lists***\n")
print ("range numbers")

# explicit range 1 up to 5
# print the first 10 cubes 1^3, 2^3, ...
print("\n=====print range =====")
for value in range (1,5):
    print(value)

print ("\n")

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====implicit range (0)=====")
# implicit starting at 0
for value in range (6):
    print (value)

print ("\n")

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====list=====")
# list of numbers
numbers = list(range(1, 6))
print(numbers)

# even numbers (start, finish, skip-by)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# exponents
squares = []
for value in range (1, 11):
    squares.append(value ** 2)

print (squares)

# count to 20
count = list(range(1, 21))
print(count)

# count to 1M
million = list(range(1, 1000000))
# for value in million:
#     print(value)

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====basic stats=====")
print(f"min of million {min(million)}")
print(f"max of million {max(million)}")
print(f"sum of million {sum(million)}")

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====odd numbers=====")
odd_numbers = list(range(1, 20, 2))
print (odd_numbers)

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====multiple of 3=====")
multiple_of_thirty = [3, 6, 9, 12, 15, 18]
for value in multiple_of_thirty :
    print(value)

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====cubes=====")
cubes = [value **3 for value in range (1, 10)]
for value in cubes :
    print(value)

# print the first 10 cubes 1^3, 2^3, ...
print("\n=====cubes=====")



