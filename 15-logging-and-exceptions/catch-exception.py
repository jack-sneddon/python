print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True :
    numerator = input("Enter the numerator: ")
    if numerator == 'q':
        break
    denominator = input("Enter the denominator: ")
    if denominator == 'q':
        break

    try:
        answer = int(numerator) / int(denominator)
    except ZeroDivisionError:
        print("You can't devide by 0!")
    except ValueError:
        print("You must enter a number")
    else:
        print(answer)
