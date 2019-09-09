# count how many words in the book 'alice in woderland'
# downloaded text through Project Gutenberg (http://gutenberg.org)

filename = '../files/alice.txt'

# split example
title = 'Alice in Wonderland'
words_in_title = title.split()
print(words_in_title)

# Count words in Alice in Wonderland
try :
    with open (filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate numer of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


        