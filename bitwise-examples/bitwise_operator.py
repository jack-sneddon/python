import array
def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5                   # number of 32 bit integers
    if (bitSize & 31):                      # if bitSize != (32 * n) add
        intSize += 1                        #    a record for stragglers
    if fill == 1:
        fill = 4294967295                                 # all bits set
    else:
        fill = 0                                      # all bits cleared

    bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

    bitArray.extend((fill,) * intSize)

    return(bitArray)



flags = 14
flagsSet = []

"""
for index in range(32) :
    if((flags & index) == index) :
        flagsSet.append(index)
"""
bits = 32
ini = 1

mybyte = bytes.fromhex("0E") # create my byte using a hex string
binary_string = "{:08b}".format(int(mybyte.hex(),16))
print(binary_string, 1)

myArray = makeBitArray(bits, ini)

# array info: input bits; final length; excess bits; fill pattern
print(bits, len(myArray), (len(myArray) * 32) - bits, bin(myArray[0]))

print(flagsSet)


