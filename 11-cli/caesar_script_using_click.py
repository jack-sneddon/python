import argparse

"""
    Use the click python package

    Arguments and options are now declared in decorators 
    which make them directly accessible as parameters of my function.



    Example: $ 
        $ python3 caesar_script_using_argparse.py --help

        $ python3 caesar_script_using_sys_argv.py --key 23 --encrypt my secret message
        $ python3 caesar_script_using_sys_argv.py --key 23 --decrypt jv pbzobq jbppxdb

     Problem: it is too verbose and programmatic whereas it could be done in 
        a more compact and declarative way. 

"""
import click

from caesar_encryption import encrypt

@click.command()

# The nargs parameter for a script argument specifies the number of successive words expected for 
# this argument (with “a quoted string like this” counting as 1 word). The default value 
# is 1. Here, nargs=-1 allow providing any number of words.
@click.argument('text', nargs=-1)
# / means mutually exclusive option
@click.option('--decrypt/--encrypt', '-d/-e')
@click.option('--key', '-k', default=1)
def caesar(text, decrypt, key):
    text_string = ' '.join(text)
    if decrypt:
        key = -key
    cyphertext = encrypt(text_string, key)
    # echo is same as print
    click.echo(cyphertext)

if __name__ == '__main__':
    caesar()