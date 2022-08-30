import pickle
import sys
import os
import re


def capitalize(name):
	#Input: string name
	#Output: name w/ capitalized first letter, lowercase all others
	return name[0].upper()+name[1:].lower()

def validate(x, pattern, err, msg):
	# Input: string x, regex pattern, string err, string msg
	# keep asking for new input until x matches the given pattern
	# Output: string x matching the pattern
	while not re.match(pattern, x):
		print(err.format(val=x))
		x = input(msg)
	return x

class Person:
	def __init__(self, last, first, mi, id_, phone):
		#Input: string last, string first, string mi, string id_, string phone
		#initialize object with proper attributes
		#Output: self
		self.last = capitalize(last)
		self.first = capitalize(first)
		self.mi = mi.upper() if mi else 'X'
		self.id = validate(id_, r'[A-Z]{2}[0-9]{4}', 
			'ID is invalid: {val}\nID is two letters followed by 4 digits',
			 'Please enter a valid ID: ')
		self.phone = validate(phone, r'[0-9]{3}-[0-9]{3}-[0-9]{4}', 
			'Phone {val} is invalid\nEnter phone number in form 123-456-7890', 
			'Enter phone number: ')

	def display(self):
		#print formatted data
		#Output: null
		print(f'Employee id: {self.id}')
		print(f'\t{self.first} {self.mi} {self.last}')
		print(f'\t{self.phone}')

def processInput(fileName):
	#Input: string fileName
	#open file and read in each line to the object
	#then return dict of people
	#Output: dict of Person objects 
	with open(os.path.join(os.getcwd(), fileName), mode='r', encoding='utf-8-sig') as inputFile:
		inputFile.readline()
		people = {}
		for line in inputFile:	
			#split attributes and pass into person constructor
			attrs = line.strip().split(',')
			p = Person(*attrs)		
			if people.get(p.id):
				# prompt for a different ID
				p.id = input('Error: Multiple IDs. Enter a different ID: ')	
			people[p.id] = p

	return people

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Insufficient arguments')

	#process input based on given file name
	people = processInput(sys.argv[1])
	#dump dict to pickle file
	pickle.dump(people, open('people.p', 'wb'))

	#reopen pickle file and display output
	print('Employee list:')
	print()
	with open('people.p', 'rb') as f:
		for _,p in pickle.load(f).items():
			p.display()
			print()