# print(help(float))

# '/' indicates positional arguments
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Jack"))
print(greet("Jack", greeting = "Welcome"))


# use postional arguments to compliment keyword-arguments
def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)

print(headline("Python 3.8", "="))
print(headline("Real Python", border=":"))
print(headline("Python", "🐍", width=38))
