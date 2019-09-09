# modulo divides one number by another number and returns the remainder
print({4%3})
number = input("enter a number and I will tell you if it even or odd: ")
number = int(number)

# even or odd
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

