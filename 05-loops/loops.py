magicians = ['alice', 'david', 'carolina']

# don't forget the colon ':'
for magician in magicians:
     print (magician)

print ("\n*******\nLoop on String Lists")

for magician in magicians:
     print (f"{magician.title()}, that was a great trick!")
     print (f"I can't wait to see your next trick, {magician.title()}")
     print ("\n")

print ("\nThank you everyone, that was a great magic show!")

# Loop through two lists at once
print ("\n*******\nPrint two lists at once!")
print ("\nPrint out two lists - even and odd !")
odds = [1,3,5,7,9]
evens = [2,4,6,8,10]
for oddnum, evennum in zip(odds,evens):
    print(oddnum)
    print(evennum)

# In Range: Write a C-Style Loop
print ("\n*******\nC-Style loop - Print out numbers 1 - 10")
for i in range(10):
    print(i)

# Enumerate(): Index your dims
print ("\n*******\n# Enumerate(): Index your dims")
l = [5,10,15]
print(f"[{l[0]},{l[1]},{l[2]}]")
# print(l[0])
# print(l[2])

# notice the type of the variable is a tuple
print(f"notice the type of variable pulled")
for i in enumerate(l):
     print(type(i))
     print(i)

# if I want it into a dictionary instead...
data = dict(enumerate(l))
print(f"{data}")

# Sorted(): Sort your data during, not before.
print ("\n*******\nSorted(): Sort your data during, not before.")
'''
The sort method is an essential method for anyone dealing with copious amount of data, 
as a Data Scientist often should. Sorting works how expected, with strings being sorted 
in alphabetical order from the letter A to the letter B, and sorting integers and doubles 
ascending from -∞. An important note to make about this function is that it will not work 
with lists containing strings and integers or floats.
'''
l = [15,6,1,8]
for i in sorted(l):
    print(i)

print("reverse the sort")
for i in sorted(l,reverse = True):
    print(i)

'''
And for the last parameter available to us, we can use a key. A key is a function that is 
applied to each dim inside of a given loop. For this, I like to use lambda, which will
create an anonymous, but still callable, function.
'''
# l.sort(key=lambda s: s[::-1])

# Filter(): Only loop the data you want.
print ("\n*******\nFilter(): Only loop the data you want.")
'''
A function that will definitely help the performance side of things when working with 
heaps of data is the filter function. The filter function does exactly what you’d expect, 
and filters out data prior to iterating over it. This can be useful when you only want to 
have an effect on data in a certain range without ever having to apply a condition to it.
'''
people = [{"name": "John", "id": 1}, {"name": "Mike", "id": 4}, {"name": "Sandra", "id": 2}, {"name": "Jennifer", "id": 3}]
for person in filter(lambda i: i["id"] % 2 == 0, people):
     print(person)

{'name': 'Mike', 'id': 4}
{'name': 'Sandra', 'id': 2}

