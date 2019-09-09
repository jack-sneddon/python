# count how many words in a file
def count_words(filename):
    """Count the approximate number of words in a file."""

    try :
        with open (filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # rather than make a big deal - aka - print(f"Sorry, the file {filename} does not exist.")
        # just continue on
        pass
    else:
        # Count the approximate numer of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['../files/alice.txt', '../files/siddhartha.txt', '../files/removed.txt', '../files/moby_dick.txt', '../files/little_women.txt']
for filename in filenames :
    count_words(filename)