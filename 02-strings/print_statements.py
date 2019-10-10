# playing around with statements
import string

thing = 'wereduck'
place = 'werepond'
print(f"The {thing} is in the {place}")

# do some formatting
print(f"The {thing.capitalize()} is in the {place.rjust(20)}")

# width, padding and alignment is also allowed inside of f
print(f"The {thing:>20} is in the {place:.^20}")

# python 8 - print the variable name - useful for debugging
# print(f"{thing =}, {place =}")
# print(f"{thing[-4] =}, {place.title() =}")  # thing[-4:] = 'duck, place.title() = Werepond



