import pickle
import requests
import os
import re
from nltk import sent_tokenize
from bs4 import BeautifulSoup

if __name__=='__main__':
	# 1) My initial webpage is an ESPN article on a hard hit that occurred in the NFL. 
	#    I request the html, then parse the contents using beautifulsoup. 
	#    I extract all the URLs and then append them to the urls array.
	URL = 'https://www.espn.com/nfl/story/_/id/34761662/dolphins-teddy-bridgewater-protocol-hard-hit'

	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	wikipediaCount = 0
	urls = []
	for text in soup.find_all('div'):
		for links in text.find_all('a'):
			link = links.get('href')
			if link is not None and link[:8] == 'https://':
				urls.append(link)


	# 2) The following cell loops through all the previously generated URLs and scrapes text off each page. 
	#    The data is then pickled and dumped into the "data" directory
	data = {}
	for url in urls:
		data[url] = []
		p = requests.get(url)
		soup2 = BeautifulSoup(p.content, 'html.parser')
		for post in soup2.find_all('p'):
			data[url].append(post.get_text())
		pickle.dump(data[url], open(f'data/{hash(url)}.p', 'wb'))


	# 3) The following cell cleans up the text for each file and outputs a pickle file in the clean_data directory. 
	#    In order to remove whitespace from the corpus, I use a regular expression to replace all whitespace with a single space
	sentences = {}
	for url, val in data.items():
		sentences[url] = []
		for text in val:
			text = re.sub(r'\s+', ' ', text)
			text = text.lower()
			sentences[url].extend(sent_tokenize(text))
		pickle.dump(data[url], open(f'clean_data/{hash(url)}.p', 'wb'))


	# 4) The following cell parses the data we've extracted. I first add every sentence in our dataset to the corpus. 
	#    Then, I convert the corpus to tokens and filter out any tokens less than length 4. 
	#    I noticed that the terms of service at the bottom of the website heavily skew the tokens towards words in the terms of service, so I added this string to a whitelist filter
	corpus = ""
	for url, sents in sentences.items():
		for sent in sents:
			corpus += sent 

	EULA = "Terms of Use Privacy Policy Your California Privacy Rights Children Online Privacy Policy Interest Based Ads About Nielsen Measurement Do Not Sell My Personal Information Contact Us Disney Ad Sales Site Work for ESPN Copyright : © ESPN Enterprises Inc. All rights reserved"
	EULA = EULA.lower()
			
	word_filter = set(stopwords.words('english') + list(string.punctuation) + EULA.split(' '))
	tokens = [t for t in word_tokenize(corpus) if len(t) > 3 and t not in word_filter]
	counts = Counter(tokens)
	counts.most_common(40)

	# 5) The most important words are as follows:
	# game, required, digital, dispute, york, south, tagovailoa, concussion, united, subject
	
	# 6) I then create the knowledge base.
	words = ['game', 'required', 'digital', 'dispute', 'york', 'south', 'tagovailoa', 'concussion', 'united', 'subject']
	knowledge_base = {}
	for word in words:
		#Find every occurrence of the word in the corpus
		res = [i.start() for i in re.finditer(word, corpus)]
		#Add the containing sentence to the knowledge base
		# Substring from previous period to the next period
		knowledge_base[word] = [corpus[corpus[:p].rfind('.')+1: corpus.find('.', p+1)] \
								  for p in res]

	# Test KB
	print(f"Fun fact: {knowledge_base['game'][2]}!\n")
	print(f"Fun fact: {knowledge_base['tagovailoa'][0]}!\n")
	print(f"Fun fact: {knowledge_base['concussion'][1]}!\n")