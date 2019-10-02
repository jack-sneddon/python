def bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

value = input("enter a number: ")
number = int(value, 10)

for b in bits(number):
    print(f"{b}")

print("\n")
print(f"{bin(number)}")


# 1000000000000000000000000000010000000000000000000000001000010010