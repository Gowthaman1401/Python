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
    parser = optparse.OptionParser(' [-c choice] [-t message]\n\t[-h help]')
    parser.add_option("-t", "--message", dest="message", help="Enter the message/code or file(with path)")
    parser.add_option("-c", "--choice", dest="choice", help="Enter the choice(Encode/Decode)")
    (options, argument) = parser.parse_args()
    if not options.choice and options.message:
        parser.error("Please specify your choice(e/d) and your message, Use --help for more info" + style.RESET)
    if not options.message:
        parser.error("Please specify your message, Use --help for more info" + style.RESET)
    if not options.choice:
        parser.error("Please specify your choice(e/d), Use --help for more info" + style.RESET)
    return options


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


# function to save output as .txt file

def save_text(filename, txt):
    path = input(style.BLUE + "Enter the path to save Text file : ")
    with open(str(path) + str(filename), "a+") as text:
        text.seek(0)
        # check whether .txt file is either empty or not
        if len(text.read()) > 0:
        # if file is not empty, write the output in next line
            text.write("\n")
        text.write(txt)
    print(style.YELLOW + "[+] Encoded/Decoded message saved in", str(path) + str(filename), style.RESET)


# function to convert string into base64 format

def base64_encode(message):
    # convert String to base64
    txt = (base64.b64encode(message.encode("ascii"))).decode("ascii")
    print(style.YELLOW + "[+] Message encoded" + style.RESET)
    # call save_text() to save the encoded message as .txt file
    save_text("Base64en.txt", txt)


# function to convert base64 into String format

def base64_decode(message):
    # convert base64 into String
    txt = (base64.b64decode(message.encode("ascii"))).decode("ascii")
    print(style.YELLOW + "[+] Message decoded" + style.RESET)
    # call save_text() to save the decoded message as .txt file
    save_text("Base64de.txt", txt)


# function to encrypt the string into morse code according to the morse code chart

def morse_encode(message):
    text = ''
    for letter in message:
        if letter != ' ':
            # looks up the dictionary and adds the corresponding morse code along with a space to separate morse codes for different characters
            text += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters and 2 indicates different words
            text += ' '
    print(style.YELLOW + "[+] Message encoded" + style.RESET)
    # call save_text() to save the encoded message as .txt file
    save_text("Morse_encode.txt", text)


# Function to decrypt the morse code into string according to the morse code chart
def morse_decode(message):
    # extra space added at the end to access the last morse code
    message += ' '
    text = ''
    text = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            i = 0
            # storing morse code of a single character
            text += letter
        else:
            i += 1
            if i == 2:
                # adding space to separate words
                text += ' '
            else:
                # accessing the keys using their values
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                          .values()).index(text)]
                text = ''
    print(style.YELLOW + "[+] Morse decoded" + style.RESET)
    # Call save_text() to save the decoded message as .txt file
    save_text("Morse_decode.txt", text)


def choice(message, choice):
    # If your choose to encode then following block
    if choice == 'Encode' or choice == 'encode' or choice == 'e' or choice == '1':
        opt = input(style.GREEN + "1.Base64\t2.Morse" + style.BLUE + "\nEnter your choice : ")
        if opt == '1' or opt == 'Base64':
            base64_encode(message)
        elif opt == '2' or opt == 'Morse':
            try:
                morse_encode(message.upper())
            except:
                print(style.RED + "[-] Invalid character found" + style.RESET)
        else:
            print(style.RESET)
            quit()

    # If your choose to decode then following block
    elif choice == 'Decode' or choice == 'decode' or choice == 'd' or choice == '2':
        opt = input(style.GREEN + "1.Base64\t2.Morse" + style.BLUE + "\nEnter your choice : ")
        if opt == '1' or opt == 'Base64':
            base64_decode(message)
        elif opt == '2' or opt == 'Morse':
            # Decoded morse code will always be in capital letters
            print(style.RED + "[-] Decoded Text will be in capital letters" + style.RESET)
            morse_decode(message)
        else:
            print(style.RESET)
            quit()


options = get_argument()
choice(options.message, options.choice)
