#!usr/bin/env python

import os, optparse, subprocess

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
    parser = optparse.OptionParser(' [-c choice] [-t message]\n\t[-h help]')
    parser.add_option("-m", "--message", dest="message", help="Enter the message")
    parser.add_option("-c", "--choice", dest="choice", help="Enter the choice(Encode/Decode)")
    parser.add_option("-p", "--path", dest="path", help="Enter the path to save .txt file" + style.RESET)
    (options, argument) = parser.parse_args()
    if not options.choice and options.message:
        parser.error(style.RED + "Please specify your choice(e/d) and your message, Use --help for more info" + style.RESET)
    if not options.message:
        parser.error(style.RED + "Please specify your message, Use --help for more info" + style.RESET)
    if not options.choice:
        parser.error(style.RED + "Please specify your choice(e/d), Use --help for more info" + style.RESET)
    return options


# function to save output as .txt file

def save_text(filename, txt, path):
    #path = input(style.BLUE + "Enter the path to save Text file : ")
    with open(str(path) + str(filename), "a+") as text:
        text.seek(0)
        # check whether .txt file is either empty or not
        if len(text.read()) > 0:
        # if file is not empty, write the output in next line
            text.write("\n")
        text.write(txt)
    print(style.YELLOW + "[+] Encoded/Decoded message saved in", str(path) + str(filename), style.RESET)


# dictionary representing the morse code chart

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# function to encrypt the string into morse code according to the morse code chart

def morse_encode(message, path):
    encoded = ''
    for letter in message:
        if letter != ' ':
            # looks up the dictionary and adds the corresponding morse code along with a space to separate morse codes for different characters
            encoded += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters and 2 indicates different words
            encoded += ' '
    print(style.YELLOW + "[+] Message encoded" + style.RESET)
    # call save_text() to save the encoded message as .txt file
    save_text("Morse_encode.txt", encoded, path)


# Function to decrypt the morse code into string according to the morse code chart
def morse_decode(message, path):
    # extra space added at the end to access the last morse code
    message += ' '
    decoded = '' 
    text = '' 
    for letter in message:
        # checks for space
        if (letter != ' '):
            i = 0
            # storing morse code of a single character
            text += letter  
        else:  
            i += 1 
            if i == 2 :
                # adding space to separate words
                decoded += ' '
            else:
                # accessing the keys using their values
                decoded += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(text)] 
                text = '' 
    print(style.YELLOW + "[+] Morse decoded" + style.RESET)
    save_text("Morse_decode.txt", decoded, path)


def choice(message, choice, path):
    if not path:
        path = os.getcwd()
    # If your choose to encode then following block
    if choice == 'Encode' or choice == 'encode' or choice == 'e' or choice == '1':
        morse_encode(message.upper(), path)

    # If your choose to decode then following block
    elif choice == 'Decode' or choice == 'decode' or choice == 'd' or choice == '2':
        morse_decode(message, path)
    else:
        print(style.RESET)
        quit()


options = get_argument()
choice(options.message, options.choice, options.path)
