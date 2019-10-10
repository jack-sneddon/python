# print statements
import string

# notice the spaces it prints
print("Give", "me", "some", "space")

print("Good Morning Jack\nThanks you too!")

print("This is another way to concatinate a string" + " with another string.")

# use '*' to duplicate a string and takes precidence over '+'
start = 'Na' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'

print(start + middle + end)

# treat a string like an array
letters = 'abcdefghijklmnopqrstuvwxyz'
print(f"The fifteenth letter in the alphabet is '" + letters[14] + "'")
print(f"The eigth letter in the alphabet is '" + letters[9] + "'")
print(f"The twenty-six letter in the alphabet is '" + letters[25] + "'")

#strings are immutable
try :
    letters[5] = 'Z'
except TypeError :
    print('Error - cannot change a string once it has been set.')
    pass

#
# substring with slice
#
letters = 'abcdefghijklmnopqrstuvwxyz'

# [:] extrac the entire sequence fro start to end
print(f"letters[:] = {letters[:]}")

# [start:] specifies from beginning to the end offset minus 1
print(f"letters[20:] = {letters[20:]}")
print(f"letters[10:] = {letters[10:]}")
print(f"letters[-3:] = {letters[-3:]}")

# [:end] specifies from beggining to the end of the offset minus 1
print(f"letters[:14] = {letters[:14]}")
print(f"letters[:5] = {letters[:5]}")

# [start:end] indicates from teh start offset to the end offset minus 1
print(f"letters[12:15] = {letters[12:15]}")
print(f"letters[15:-2] = {letters[15:-2]}")
print(f"letters[-5:-2] = {letters[-5:-2]}")

# [start:end:step] extracts from the start offset to the end offset minus 1, 
# skipping characters by step
print(f"letters[::2] = {letters[::2]}")
print(f"letters[1::2] = {letters[1::2]}")
print(f"letters[1:19:2] = {letters[1:19:2]}")
print(f"letters[:21:5] = {letters[:21:5]}")
print(f"letters[-1::-1] = {letters[-1::-1]}")
print(f"letters[::-1] = {letters[::-1]}")
print(f"letters[-50::] = {letters[-50::]}")
print(f"letters[:21:5] = {letters[:70]}")

# get a string length
string_len = len(letters)
print(f"string length of '{letters}' is {string_len}")

# 'split' a string into a list
tasks = 'get gloves, get masks, get helmet, get skis, get gas, call dinner reservations'
tasks_list = tasks.split(',')  # without any arguments, splits on any whitespace
print(tasks_list)

# 'join' a list to a string
tasks_string = ', '.join(tasks_list)
print(f"Things to get done on ski day:", tasks_string)

# 'replace' aka string substitution
setup = "a duck goes into a bar..."
print(setup.replace("duck", "panda"))
print(setup)

# 'replace can be trouble if I don't know the exact string to replace.  
# it overwrites -- use regular expressions when I want to replace a word
print("replace overwrites... be careful 'a duck goes into a bar... replace 'a' with 'a famous'")
print("\t", setup.replace('a', 'a famous', 100))  

# strip - cut out leading or trailing characters
world = '     mars    '
print (world)
print(world.strip())
print(world.strip(' '))
print (world.lstrip())
print(world.rstrip())
print(world.strip("!")) # will be ignored because it is not found

i_swear = "holy @#$!%^$#"
print(i_swear.strip('!%'))

# some helpful whitespace
# print(f"'{string.whitespace}''")
print(f"'{string.punctuation}''")
print(i_swear.strip(string.punctuation))

i_declare = "    I do declare...   @@#%@^#$%"
print(i_declare.strip(string.whitespace + string.punctuation))

#
# analyze a longer string
#
poem = '''All that doth flow we cannot liquid name
... Or else would fire and water be the same;
... But that is liquid which is moist and wet
... Fire that property can never get.
... Then 'tis not cold that doth the fire put out
... But 'tis the wet that makes it die, no doubt.'''

print(f"Start of the poem is : {poem[:13]}")
print(f"length of the poem: {len(poem)}")

# startswith / endswith
print(f"Does the poem start with 'All?' {poem.startswith('All')}")
print(f"Does the poem end with 'The end?' {poem.endswith('The end!')}")

# find and index - find the offset of a substring
# if not found, find returns -1, index throws an exception

word = 'the'

# find the first occurence
print(poem.find(word))
print(poem.index(word))

# find the last occurence
print(poem.rfind(word))
print(poem.rindex(word))

# not found
word = 'utah'
try:
    print(poem.find(word))
    print(poem.index(word))
except :
    print(f"{word} not found!  Exception caught.") 
    pass

# how many three letter sequence
word = 'the'
print(f"how many times does the letter sequence '{word}'' occur? {poem.count(word)}")

# letters or numbers?
print(f"are all the characters in the poem either letters or numbers?", poem.isalnum())


# Case functions
print(setup)
# capitalize first letter as in a title
print("title() - ", setup.title())
# upper case
print("upper() - ", setup.upper())
# lower case
print("lower() - ", setup.lower())
# swap upper and lower case
print("swapcase() - ", setup.swapcase())

#
# layout alignment functions
#

# center string with 30 spaces
print(setup.center(30))
# left justify
print(setup.ljust(30))
# right justify
print(setup.rjust(30))

# Formatting - useful for creating reports
# old style - '%'
# new style 
# newest style - f-string - 



