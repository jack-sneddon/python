import click

"""
    Adding some confidentiality (improved version of click)
    Our script arguments are supposed to be top secret messages that will 
    be encrypted. Isn’t it ironic to ask the user to type his plain texts 
    directly in his terminal, leaving them in his commands history?

    A solution to do it in a more secure way is to use a hidden prompt. 
    
    Or we could read the text from an input file, which would be much 
    more practical for long texts. 
    
    Or why not let the choice to the user?

"""

from caesar_encryption import encrypt

@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    help='File in which there is the text you want to encrypt/decrypt.'
         'If not provided, a prompt will allow you to type the input text.',
)
@click.option(
    '--output_file',
    type=click.File('w'),
    help='File in which the encrypted / decrypted text will be written.'
         'If not provided, the output text will just be printed.',
)
@click.option(
    '--decrypt/--encrypt',
    '-d/-e',
    help='Whether you want to encrypt the input text or decrypt it.'
)
@click.option(
    '--key',
    '-k',
    default=1,
    help='The numeric key to use for the caesar encryption / decryption.'
)
def caesar(input_file, output_file, decrypt, key):
    if input_file:
        text = input_file.read()
    else:
        text = click.prompt('Enter a text', hide_input=not decrypt)
    if decrypt:
        key = -key
    cyphertext = encrypt(text, key)
    if output_file:
        output_file.write(cyphertext)
    else:
        click.echo(cyphertext)

if __name__ == '__main__':
    caesar()