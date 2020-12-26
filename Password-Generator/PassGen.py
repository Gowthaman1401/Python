#!usr/bin/env python

import os
import optparse
import random
import subprocess

def get_argument():
    parser = optparse.OptionParser(' [-l length] [-i include] [-o wanted_characters] [-n unwanted_characters] [-r repeat_characters(Y/N)] [-h help]')
    parser.add_option("-l", "--length", dest="length", help="Length to the password")
    parser.add_option("-n", "--no", dest="no", help="Unwanted characters to the password")
    parser.add_option("-i", "--include", dest="include", help="Include characters to the password")
    parser.add_option("-o", "--only", dest="only", help="Only wanted characters to the password")
    parser.add_option("-r", "--repeat", dest="repeat", help="Repeat the characters in the password")
    (options, argument) = parser.parse_args()
    return options

def wanted_characters(characters):
	possibility = ''
	try:
		character = [character for character in characters.split(',')]
	except:
		pass
	for choice in character:
		if choice.lower() == 'alphabets':
			possibility += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if choice.lower() == 'lowercase':
			possibility += 'abcdefghijklmnopqrstuvwxyz'
		if choice.lower() == 'uppercase':
			possibility += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if choice.lower() == 'numbers':
			possibility += '0123456789'
		if choice.lower() == 'symbols':
			possibility += str('''!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\''')
		if not choice.lower() in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
			for unwanteds in choice:
				possibility += unwanteds
	return possibility

def include_characters(adding ,characters):
	possibility = characters
	try:
		character = [character for character in adding.split(',')]
	except:
		pass
	for choice in character:
		if choice.lower() == 'alphabets':
			for alphabet in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
				if alphabet not in possibility:
					possibility += alphabet
		if choice.lower() == 'lowercase':
			for alphabet in "abcdefghijklmnopqrstuvwxyz":
				if alphabet not in possibility:
					possibility += alphabet
		if choice.lower() == 'uppercase':
			for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				if alphabet not in possibility:
					possibility += alphabet
		if choice.lower() == 'numbers':
			for number in "0123456789":
				if number not in possibility:
					possibility += number
		if choice.lower() == 'symbols':
			for symbol in str('''!"%&'()*+,-./:;<=>?@[]^_`{|}~”$‘~#\\'''):
				if symbol not in possibility:
					possibility += symbol
		if not choice.lower() in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
			for unwanteds in choice:
				if unwanteds not in possibility:
					possibility += unwanteds
	return possibility

def unwanted_characters(unwanted, possibility):
	unwanted_lists, unwanted_characters_lists = '', ''
	try:
		choices = [characters for characters in unwanted.split(',')]
	except:
		pass
	if unwanted == ',' or ',,,' in unwanted or ',,' in unwanted:
		possibility = possibility.replace(',', '')
	for choice in choices:
		if choice == 'alphabets':
			for alphabet in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
				possibility = possibility.replace(alphabet, '')
		if choice == 'uppercase':
			for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				possibility = possibility.replace(alphabet, '')
		if choice == 'lowercase':
			for alphabet in "abcdefghijklmnopqrstuvwxyz":
				possibility = possibility.replace(alphabet, '')
		if choice == 'numbers':
			for number in "0123456789":
				possibility = possibility.replace(number, '')
		if choice == 'symbols':
			for symbol in str('''!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\'''):
				possibility = possibility.replace(symbol, '')
		if not choice in ['numbers', 'alphabets', 'uppercase', 'lowercase', 'symbols']:
			for unwanteds in choice:
				possibility = possibility.replace(unwanteds, '')
	return possibility

def pass_gen(length, choice, charac, include, repeat):
	possibility = str('''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"%&'()*,+-./:;<=>?@[]^_`{|}~”$‘~#\\''')
	if choice:
		if charac:
			possibility = wanted_characters(charac)
		if include:
			possibility = include_characters(include, possibility)
		possibility = unwanted_characters(choice.lower(), possibility)
	else:
		if charac:
			possibility = wanted_characters(charac)
		if include:
			possibility = include_characters(include, possibility)
	if repeat is None or repeat.lower() == 'y':
		repeat = 'y'
	if not length:
		length = random.randint(8, 16)
	possibility = (possibility*int(length)) if repeat.lower() == 'y' else possibility
	if length and (int(length) > len(possibility) or int(length) > 72):
		quit('\n[-] Password length must be less.')
	elif not length and charac:
		quit('\n[-] Password length must be given')
	return print("\nPassword :", "".join(random.sample(possibility, int(length))))


if __name__ == '__main__' :
	options = get_argument()
	pass_gen(options.length, options.no, options.only, options.include, options.repeat)
