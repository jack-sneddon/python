# regex tests
# regex101.com
import re
import unittest
from testRegex import TestRegex

# match objects
# https://docs.python.org/3/library/re.html#match-objects

test_regex = TestRegex()

# match to the beginning of a string

# search for any match where it starts with the string
check_strings = ['a258035', 'A258035', 
    'aa258035', '258035', 'a25803A', 
    'a25803A', 'a2580333312341233']

for check_string in check_strings :
    match = False    
    matches = re.match(r"^[Aa]([0-9]{6})", check_string)

    if matches == None :
        match = False
    else :        
        match = True
        print(matches.group(0))
        
    print(f"{check_string} match? {match}")



# test_regex Assertions
valid_string = 'a258035'
invalid_string = '258035'

matches = re.fullmatch(r"^[Aa][0-9]{6}", invalid_string)
test_regex.test_None(matches, invalid_string)

matches = re.fullmatch(r"^[Aa][0-9]{6}", valid_string)
test_regex.test_full_match_found(matches, valid_string)

matches = re.fullmatch(r"^[Aa][0-9]{6}", valid_string)
test_regex.test_match_found(matches)


# test for matching strings
name = ["A1B1", "djdd", "B2C3", "C2H2", "jdoi", "1A4V"]

# match names.
for element in name:
    m = re.match(r"(^[A-Z]\d[A-Z]\d)", element)
    if m:
        print(m.groups())
