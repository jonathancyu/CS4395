import sys
import random

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

def preprocess(raw):
	tokens = [t.lower() for t in raw if t.isalpha() and
			  t.lower() not in stopwords.words('english') and
			  len(t) > 5]
	wnl = WordNetLemmatizer()
	lemmas = set([wnl.lemmatize(t) for t in tokens])
	tags = pos_tag(tokens)
	print(f"First 20 tags: {tags[:20]}")
	nouns = [t[0] for t in tags if t[1][0]=="N"]
	print(f"Number of tokens: {len(tokens)}")
	print(f"Number of nouns: {len(nouns)}")
	return tokens, nouns

def getLocations(input, char):
	return [i for i, c in enumerate(input) if c == char]

def printCurrent(current):
	result = ""
	for c in current:
		result += c + " "
	print(result[:-1])

def guessingGame(nouns, points=5, won=False):
	if won:
		print()
		print(f"Current score: {points}")
		print("Guess another word")
	else:
		print("Let's play a word guessing game!")
	word = random.choice(nouns)
	letters = {c: getLocations(word, c) for c in set([x for x in word])}
	current = ["_"]*len(word)
	printCurrent(current)
	guess = input("Guess a letter: ")
	won = False
	while points >= 0 and guess != "!":
		if locs := letters.get(guess):
			for loc in locs:
				current[loc] = guess
			letters.pop(guess, None)
			if len(letters) == 0:
				won = True
				break
			print(f"Right! Score is {points}")
			points += 1
		else:
			print(f"Sorry, guess again. Score is {points}")
			points -= 1
		printCurrent(current)
		guess = input("Guess a letter: ")
	if won: 
		printCurrent(current)
		print("You solved it!")
		nouns.remove(word)
		guessingGame(nouns, points, won)




if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error: no file passed")
		pass

	file = open(sys.argv[1], 'r')
	tokens = []
	for line in file:
		tokens.extend([x.lower() for x in line.split()])

	tokenSet = set(tokens)
	print("Lexical diversity: %.2f" % (len(tokenSet)/len(tokens)))
	tokens, nouns = preprocess(tokens)

	count = {}
	for noun in nouns:
		if count.get(noun):
			count[noun] += 1
		else:
			count[noun] = 1

	top50 = [x[0] for x in sorted(count.items(), key=lambda item: item[1])][-50:]
	print("Most common words: ", top50)
	guessingGame(top50)
