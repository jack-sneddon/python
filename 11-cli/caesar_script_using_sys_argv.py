import sys

"""
    Enumerate through arguments of the CLI. 
    Example: 
        $ python3 caesar_script_using_sys_argv.py --key 23 --encrypt my secret message
        $ python3 caesar_script_using_sys_argv.py --key 23 --decrypt jv pbzobq jbppxdb


    This script more or less respects the recommendations stated above:

    There are a default key value and a default mode

    Basic error cases are handled (no input text provided or unknown arguments)

    A succinct documentation is printed in these error cases, and when calling the script with no argument:

    Problem -- However, this version of the Caesar script is quite long (39 lines, which doesn’t even include 
        the logic of the encryption itself) and ugly.

    


"""

from caesar_encryption import encrypt

def caesar():
    key = 1
    is_error = False

    for index, arg in enumerate(sys.argv):
        if arg in ['--key', '-k'] and len(sys.argv) > index + 1:
            key = int(sys.argv[index + 1])
            del sys.argv[index]
            del sys.argv[index]
            break

    for index, arg in enumerate(sys.argv):
        if arg in ['--encrypt', '-e']:
            del sys.argv[index]
            break
        if arg in ['--decrypt', '-d']:
            key = -key
            del sys.argv[index]
            break

    if len(sys.argv) == 1:
        is_error = True
    else:
        for arg in sys.argv:
            if arg.startswith('-'):
                is_error = True

    if is_error:
        print(f'Usage: python {sys.argv[0]} [ --key <key> ] [ --encrypt|decrypt ] <text>')
    else:
        print(encrypt(' '.join(sys.argv[1:]), key))

if __name__ == '__main__':
    caesar()