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


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        two_words = (words[i], words[i + 1])

        if two_words in chains: 
            chains[two_words].append(words[i + 2])
        else:
            chains[two_words] = [words[i + 2]]
  
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    bi_gram, next_words = choice(list(chains.items()))

    for gram in bi_gram:
        words.append(gram)

    words.append(choice(next_words))

    while True: 
        if (words[-2], words[-1]) in chains:
            next_combo = chains[(words[-2], words[-1])]
            words.append(choice(next_combo))
        else:
            break

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

