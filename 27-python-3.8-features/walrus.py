"""
assignment expressions
walrul operator (:=) allow you to assign and return a value in the same expression
"""

# old way
walrus = False
print(walrus)

# new way
print(walrul:=False)

# a little clumsy
inputs = list()
current = input("Write something: ")
while current != "quit":
    inputs.append(current)
    current = input("Write something: ")

# with the walrus
inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)




