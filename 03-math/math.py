# math play

#
# print numbers
#

myNumber = 125
print("[print via str()]\n\t" + str(myNumber))
print("[print via %% operator]\n\t%s" %myNumber)
print("[print via format function]\n\t{}".format(myNumber))
print(f'[print via f function\n\t{myNumber}')


# integers
print('[operators]')
myInt1 = 10
myInt2 = 5

myAdd = myInt1 + myInt2
mySub = myInt1 - myInt2
myMult = myInt1 * myInt2
myDiv = myInt1 / myInt2
print(f"\t {myInt1} + {myInt2} = {myAdd}")
print(f"\t {myInt1} - {myInt2} = {mySub}")
print(f"\t {myInt1} * {myInt2} = {myMult}")
print(f"\t {myInt1} / {myInt2} = {myDiv}")

# underscores in numbers - long numbers you can group digits with underscors
# python ignores uncerscores - 1000 = 10_00 = 1_000 
universal_age = 14_000_000_000
print(f"universal age = {universal_age}")

## multiple assignments 
print("reset all calculated values")
myAdd, mySub, myMult, myDiv = 0, 0, 0, 0
print (f"myAdd = {myAdd}, mySub = {mySub}, myMult = {myMult}, myDiv = {myDiv}")

# constants - only by notation through all capital letters.  There is not constant in python
MAX_CONNEXTIONS = 5000
print(MAX_CONNEXTIONS)

