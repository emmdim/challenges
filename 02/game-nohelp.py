#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from itertools import permutations
import ipdb

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_random(pouch):
	"""Draw 7 random letters from the pouch"""
	return random.sample(pouch,NUM_LETTERS)


def validate_input(letters1, word):
	"""Validate that letters from word are from the ones drawn and
	that the word exists"""
	# Check if letters from pouch
	letters = letters1[:]
	for ch in word:
		if ch in letters:
			letters.remove(letters[letters.index(ch)])
		else:
			raise ValueError("Cheater!!!")
	#If reach here then letters are from pouch
	#Check if word is in the dictionary
	if word.lower() in DICTIONARY:
		return
	else:
		raise ValueError("Dictionary Cheater!!!")


def permutation_generator(letters):
	perms = []
	for i in range(1,NUM_LETTERS+1):
		for p in permutations(letters,i):
			if ''.join(p).lower() in DICTIONARY:
				perms.append(''.join(p).lower())
	return perms


def calculate_optimal(letters):
	perms = permutation_generator(letters)
	return max_word_value(perms)

def main():
	letters = draw_random(POUCH)
	#letters = [l.lower() for l in letters]
	print("Letters drawn: "+str(letters).strip('[]'))
	word = raw_input("Form a valid word: ").upper()
	validate_input(letters, word)
	score = calc_word_value(word)
	print('Word Chosen: {} (value: {})'.format(word,str(score)))
	optimal_word = calculate_optimal(letters)
	optimal_score = calc_word_value(optimal_word) 
	final_score = 1.*score/optimal_score * 100
	print("Optimal word possible: "+optimal_word.upper()+' (value: '+str(optimal_score)+')')
	print("You scored: {0:.3}".format(final_score))


if __name__ == "__main__":
    main()
