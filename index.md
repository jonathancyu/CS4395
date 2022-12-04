## Welcome to my portfolio
I'm a computer science student at UT Dallas! I love to read, cook, play video games, and a whole lot of other stuff.

## Portfolio Objective
This portfolio highlights work done for the [Introduction to Natural Language Processing](https://github.com/kjmazidi/NLP/blob/gh-pages/index.md) class at UTD with Professor Karen Mazidi. 

## Portfolio Contents
1. [Overview of NLP](https://jonathancyu.github.io/Component0/Overview%20of%20NLP.pdf)

2. [Python Warmup](https://jonathancyu.github.io/NLP-Portfolio/homework1/homework1_jcy180000.py)
	* This program imports data from a .csv file, and then validates the given info. If any values are not formatted correctly, the program prompts for a correct entry. The program then saves the data as a pickle file, then loads the same pickle file and prints the data.
	In order to run the program, enter 
	```python homework1_jcy180000.py data/data.csv```
	In my opinion, Python is incredibly powerful for text processing. However, Python is not built for optimal runtime thus text processing could be faster in some other languages. This can be said for any function or library of Python.
	This assignment was mostly review for me. One thing I learned is how powerful pickle files are. Initially, I thought they were simply json files under a different name, however I soon realized it's a way to save an object with all of its components, which is incredibly useful.

3. [NLTK Intro](https://jonathancyu.github.io/NLP-Portfolio/homework2/homework2.pdf)
	* This is a PDF of a Jupyter notebook containing the exercises from the homework 2 NLTK intro. 

4. [Guessing Game](https://github.com/jonathancyu/NLP-Portfolio/tree/main/guessinggame)
	* This program parses the first chapter of an anatomy textbook. It computes the lexical diversity and top 50 nouns, then creates a hangman-esque guessing game with them. Execute this with
	```python main.py anat19.txt```
	
	To exit the game, enter !.

5. [WordNet Intro](https://jonathancyu.github.io/NLP-Portfolio/wordnet/WordNet.pdf)
	* This is a PDF of a Jupyter notebook containing the exercised from the WordNet introductory assignment.

6. NGrams [Problem 1](https://jonathancyu.github.io/NLP-Portfolio/ngrams/Problem1.py) [Problem 2](https://jonathancyu.github.io/NLP-Portfolio/ngrams/Problem2.py)
	* In this assignment I worked with a partner to create a Naive Bayes' classifier to determine the most likely language of a given sentence.

7. [Web Crawler](https://jonathancyu.github.io/NLP-Portfolio/webcrawler/KnowledgeBase.pdf)
	* In this assignment I use a web crawler to scrape data off ESPN articles in order to create a knowledge base containing sports terms.

8. [Sentence Parsing](https://jonathancyu.github.io/NLP-Portfolio/sentenceparsing/sentenceparsing.pdf)
	* In this assignment, I explore the pros and cons of PSG trees, dependency parsing, and SRL parsing. From my experience, I've found that dependency parsing extracts the most value from the sentence.
9. [Author Attribution](https://jonathancyu.github.io/NLP-Portfolio/authorattribution/authorattribution.pdf)
	* In this assignment, I use Naive-Bayes, Logistic Regression, as well as Neural Networks to predict the authors of the Federalist papers. I found that the highest accuracy was about 94%, which was achieved by both the Naive-Bayes classifier as well as the Neural Network.
10. [Keras Text Classification](https://jonathancyu.github.io/NLP-Portfolio/textclassification/textclassification.pdf)
	* This has been my favorite assignment of the semester. In this assignment, I used varying Neural Network architectures to classify the fake news dataset from kaggle.com. I found that a simple sequential neural network model fit this task the best given the limited compute on my local machine.