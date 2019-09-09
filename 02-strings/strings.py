######### string replacements
message = "hello pythong world"
print (message)
message = "this is replacement of the sting"
print (message)
message = 'this string has "embedded quotes"'
print (message)
message = "this string's apostrophes is printed"
print (message)

# replace a word in a string
message = "I really like dogs."
# message = message.replace('dog', 'cat')
print(f"{message.replace('dog', 'cat')}")

######### convert case
name = 'Peyton sNeddon'
print ("Name to upper: " + name.upper())
print ("Name to lower: " + name.lower())
print ("Name title: " + name.title())

######### add a variable to a string
# f strings are only for Python 3.6 and later
first_name = "Amelia"
last_name = "sneddon"
full_name = f"{first_name} {last_name}"
# compose a string from the variables
message = f"Hello, {full_name.title()}!"
print (message)

# < Python 3.6
# use of "format" to do substitution.
# full_name = "{}{}".format(first_name, last_name)

# tabs and newlines
print("\t[tab] hello-world")
print("[new line]\n\thello\n\tworld")

# remove whitepace
print ("[trim leading/trailing whitespace]")
whitespace_string = "   stuff   "
message = f"\t'{whitespace_string}'"
print (message)
message = f"\t'{whitespace_string.rstrip()}'"
print (message)
message = f"\t'{whitespace_string.lstrip()}'"
print (message)
message = f"\t'{whitespace_string.lstrip().rstrip()}'"
print (message)
whitepsace_string = whitespace_string.lstrip().rstrip()
print ("\t" + whitepsace_string)

