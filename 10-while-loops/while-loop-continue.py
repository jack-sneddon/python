# use a continue within th while loop
current_number = 0

#print odd numbers
while current_number < 10:
    current_number +=1
    if current_number %2 == 0:
        continue

    print(current_number)

