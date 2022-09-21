import sys
import random

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

def preprocess(raw):
	#Confirm tokens are alpha, long enough, and not stop words
	tokens = [t for t in raw if t.isalpha() and
			  t not in stopwords.words('english') and
			  len(t) > 5]
	wnl = WordNetLemmatizer()

	#Lemmatize and tag the tokens
	lemmas = set([wnl.lemmatize(t) for t in tokens])
	tags = pos_tag(tokens)
	print(f"First 20 tags: {tags[:20]}")

	# t is a noun if the first letter of its tag is an "N"
	nouns = [t[0] for t in tags if t[1][0]=="N"]
	print(f"Number of tokens: {len(tokens)}")
	print(f"Number of nouns: {len(nouns)}")
	return tokens, nouns

def getLocations(word, char):
	#Takes in a word and a character. Returns a list containing all locations of the character in the word
	return [i for i, c in enumerate(word) if c == char]

def printCurrent(current):
	#Format the "current" list
	result = ""
	for c in current:
		result += c + " "
	print(result[:-1])

def guessingGame(nouns, points=5, won=False):
	if won:
		#This is called if we've already won the game.
		print()
		print(f"Current score: {points}")
		print("Guess another word")
	else:
		print("Let's play a word guessing game!")
	
	#Choose a random word
	word = random.choice(nouns)
	
	#Compute the locations for each letter
	letters = {c: getLocations(word, c) for c in set([x for x in word])}

	#Display current process by printing this list
	current = ["_"]*len(word)
	printCurrent(current)
	guess = input("Guess a letter: ")
	won = False
	while points >= 0 and guess != "!":
		# If the guess is in letter
		if locs := letters.get(guess):
			#Fill in current w/ letter
			for loc in locs:
				current[loc] = guess

			#Remove letter from letters
			letters.pop(guess, None)
			if len(letters) == 0:
				#If there's nothing left in letters, we won.
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
		#Remove word from nouns so we don't try to guess it again
		nouns.remove(word)
		guessingGame(nouns, points, won)




if __name__ == "__main__":
	#Check for proper args
	if len(sys.argv) != 2:
		print("Error: no file passed")
		pass

	#read in file
	file = open(sys.argv[1], 'r')
	#convert tokens to lower
	tokens = []
	for line in file:
		tokens.extend([x.lower() for x in line.split()])

	#Compute lexical diversity
	tokenSet = set(tokens)
	print("Lexical diversity: %.2f" % (len(tokenSet)/len(tokens)))

	tokens, nouns = preprocess(tokens)

	#Compute noun counts
	count = {}
	for noun in nouns:
		if count.get(noun):
			count[noun] += 1
		else:
			count[noun] = 1
	#Sort count by value, then take the last 50 elements
	top50 = [x[0] for x in sorted(count.items(), key=lambda item: item[1])][-50:]
	print("Most common words: ", top50)
	#Begin the game
	guessingGame(top50)
