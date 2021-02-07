import sys

"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - n):
        n_gram = []
        for num in range(i,i+n): 
            n_gram.append(words[num])
        
        n_gram = tuple(n_gram)  
        
        if n_gram in chains: 
            chains[n_gram].append(words[i + n])
        else:
            chains[n_gram] = [words[i + n]]

    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    while True:
        n_gram, next_words = choice(list(chains.items()))
        if n_gram[0][0].isupper():
            break
        else:
            continue

    for gram in n_gram:
        words.append(gram)

    words.append(choice(next_words))

    while True:
        n_gram = []
        for i in range(n):
            n_gram.append(words[-(i+1)])
        if tuple(n_gram[::-1]) in chains and tuple(n_gram[::-1])[-1][-1] in ['.','!','?']:
            break
        elif tuple(n_gram[::-1]) in chains:
            next_combo = chains[tuple(n_gram[::-1])]
            words.append(choice(next_combo))
        else:
            break

    return ' '.join(words)


input_path_1 = sys.argv[1]
input_path_2 = sys.argv[2]

# Open the file and turn it into one long string
input_text_1 = open_and_read_file(input_path_1)
input_text_2 = open_and_read_file(input_path_2)
input_text = input_text_1 + input_text_2

# Get a Markov chain
chains = make_chains(input_text, 4)

# # Produce random text
random_text = make_text(chains, 4)

print(random_text)

