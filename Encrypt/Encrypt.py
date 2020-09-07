#!usr/bin/env python

import os, optparse, base64, subprocess

# provide colors to output which helps to identify output easily

os.system('')

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# function to get inputs and helps when you got stuck

def get_argument():
    print(style.RED)
    parser = optparse.OptionParser(' [-c choice] [-t messege]\n\t[-h help]')
    parser.add_option("-t", "--messege", dest="messege", help="Enter the messege/code or file(with path)")
    parser.add_option("-c", "--choice", dest="choice", help="Enter the choice(Encode/Decode)")
    (options, argument) = parser.parse_args()
    if not options.choice and options.messege:
        parser.error("Please specify your choice(e/d) and your messege, Use --help for more info" + style.RESET)
    if not options.messege:
        parser.error("Please specify your messege, Use --help for more info" + style.RESET)
    if not options.choice:
        parser.error("Please specify your choice(e/d), Use --help for more info" + style.RESET)
    return options

# dictionary representing the morse code chart 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 					
		'C':'-.-.', 'D':'-..', 'E':'.', 
		'F':'..-.', 'G':'--.', 'H':'....', 
		'I':'..', 'J':'.---', 'K':'-.-', 
		'L':'.-..', 'M':'--', 'N':'-.', 
		'O':'---', 'P':'.--.', 'Q':'--.-', 
		'R':'.-.', 'S':'...', 'T':'-', 
		'U':'..-', 'V':'...-', 'W':'.--', 
		'X':'-..-', 'Y':'-.--', 'Z':'--..', 
		'1':'.----', '2':'..---', '3':'...--', 
		'4':'....-', '5':'.....', '6':'-....', 
		'7':'--...', '8':'---..', '9':'----.', 
		'0':'-----', ', ':'--..--', '.':'.-.-.-', 
		'?':'..--..', '/':'-..-.', '-':'-....-', 
		'(':'-.--.', ')':'-.--.-'} 

# function to save output as .txt file

def savetxt(filename, txt):
	path = input(style.BLUE + "Enter the path to save Text file : ")
	with open(str(path) + str(filename),"a+") as text:
		text.seek(0)  
        # check whether .txt file is either empty or not
        data = text.read()
        if len(data) > 0 :
            # if file is not empty, write the output in next line
            text.write("\n")
        text.write(txt)
	print(style.YELLOW + "[+] Encoded/Decoded messege saved in", str(path) + str(filename), style.RESET)

# function to convert string into base64 format

def b64en(messege):
    # convert String to base64
    txt = (base64.b64encode(messege.encode("ascii"))).decode("ascii")
    print(style.YELLOW + "[+] Messege encoded" + style.RESET)
    # call savetxt() to save the encoded messege as .txt file 
    savetxt("Base64en.txt", txt)	

# function to convert base64 into String format

def b64de(messege):
    # convert base64 into String
	txt = (base64.b64decode(messege.encode("ascii"))).decode("ascii")
	print(style.YELLOW + "[+] Messege decoded" + style.RESET)
    # call savetxt() to save the decoded messege as .txt file 
	savetxt("Base64de.txt", txt)

# function to encrypt the string into morse code according to the morse code chart 

def moren(messege): 
	text = '' 
	for letter in messege: 
		if letter != ' ': 
            # looks up the dictionary and adds the correspponding morse code along with a space to separate morse codes for different characters 
			text += MORSE_CODE_DICT[letter] + ' '
		else:
            # 1 space indicates different characters and 2 indicates different words 
			text += ' '
	print(style.YELLOW + "[+] Messege encoded" + style.RESET)
    # call savetxt() to save the encoded messege as .txt file 
	savetxt("Morseen.txt", text)

# Function to decrypt the morse code into string according to the morse code chart 
def morde(messege): 
    # extra space added at the end to access the last morse code 
	messege += ' '
	text = '' 
	citext = '' 
	for letter in messege:
        # checks for space
		if (letter != ' '):
			i = 0
            # storing morse code of a single character
			citext += letter 
		else: 
			i += 1
			if i == 2 :
                # adding space to separate words
				text += ' '
			else:
				# accessing the keys using their values
				text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 
	print(style.YELLOW + "[+] Morse decoded" + style.RESET) 
    # Call savetxt() to save the decoded messege as .txt file 
	savetxt("Morsede.txt", text)

def choice(messege, choice):
	# If your choose to encode then following block
	if choice == 'Encode' or choice == 'encode' or choice == 'e' or choice == '1':
		opt = input(style.GREEN + "1.Base64\t2.Morse" + style.BLUE + "\nEnter your choice : ")
		if opt == '1' or opt == 'Base64':
			b64en(messege)
		elif opt == '2' or opt == 'Morse':
			try:
				moren(messege.upper())
			except:
				print(style.RED + "[-] Invalid character found" + style.RESET)
		else:
			print(style.RESET)
			quit()
	
	# If your choose to decode then following block
	elif choice == 'Decode' or choice == 'decode' or choice == 'd' or choice == '2':
		opt = input(style.GREEN + "1.Base64\t2.Morse" + style.BLUE + "\nEnter your choice : ")
		if opt == '1' or opt == 'Base64':
			b64de(messege)
		elif opt == '2' or opt == 'Morse':
			# Decoded morse code will always be in capital letters
			print(style.RED + "[-] Decoded Text will be in capital letters" + style.RESET)
			morde(messege)
		else:
			print(style.RESET)
			quit()

options = get_argument()
choice(options.messege, options.choice)
