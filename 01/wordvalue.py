import ipdb
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
    	return [word.strip() for word in f.read().split()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    scores = [LETTER_SCORES.get(character.upper(),0) for character in word]
    return sum(scores)
    

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words or load_words(), key = lambda l : calc_word_value(l))

if __name__ == "__main__":
	words = load_words()
	#print max_word_value()
