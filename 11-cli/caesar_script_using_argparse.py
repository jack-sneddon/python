import argparse

"""
    Use argparse to get arguments of CLI
    Example: $ 
        $ python3 caesar_script_using_argparse.py --help

        $ python3 caesar_script_using_sys_argv.py --key 23 --encrypt my secret message
        $ python3 caesar_script_using_sys_argv.py --key 23 --decrypt jv pbzobq jbppxdb

     Problem: it is too verbose and programmatic whereas it could be done in 
        a more compact and declarative way. 

"""

import argparse

from caesar_encryption import encrypt


def caesar():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=1)
    args = parser.parse_args()

    text_string = ' '.join(args.text)
    key = args.key
    if args.decrypt:
        key = -key
    cyphertext = encrypt(text_string, key)
    print(cyphertext)

if __name__ == '__main__':
    caesar()