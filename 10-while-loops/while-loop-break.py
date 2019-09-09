# use a break in the while loop
prompt = "Tell me a name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True :
    city = input(prompt)

    if city == 'quit':
        break
    else :
        print(f"I'd love to go to {city.title()}")

