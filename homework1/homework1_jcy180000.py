import pickle
import sys
import os
import re


def capitalize(name):
	#capitalize first letter, lowercase all others
	return name[0].upper()+name[1:].lower()

def validate(x, pattern, msg):
	# keep asking for new input until x matches the given pattern
	while not re.match(pattern, x):
		x = input(msg)
	return x

class Person:
	def __init__(self, last, first, mi, id_, phone):
		#initialize object with proper attributes
		self.last = capitalize(last)
		self.first = capitalize(first)
		self.mi = mi.upper() if mi else 'X'
		self.id = validate(id_, r'[A-Z]{2}[0-9]{4}', 'Please enter a valid ID: ')
		self.phone = validate(phone, r'[0-9]{3}-[0-9]{3}-[0-9]{4}', 'Please enter a valid phone number: ')

	def display(self):
		#display formatted data
		print(f'Employee id: {self.id}')
		print(f'\t{self.first} {self.mi} {self.last}')
		print(f'\t{self.phone}')

def processInput(fileName):
	#open file and read in each line to the object
	with open(os.path.join(os.getcwd(), fileName), mode='r', encoding='utf-8-sig') as inputFile:
		inputFile.readline()
		people = {}
		for line in inputFile:	
			#split attributes and pass into person constructor
			attrs = line.strip().split(',')
			p = Person(*attrs)		
			if people.get(p.id):
				p.id = input('Error: Multiple IDs. Re-enter a valid ID: ')	
			people[p.id] = p


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Insufficient arguments')
	people = processInput(sys.argv[1])
	pickle.dump(people, open('people.p', 'wb'))
	print('Employee list:')
	print()
	for _,p in pickle.load(open('people.p', 'rb')).items():
		p.display()
		print()