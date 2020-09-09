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
    parser.add_option("-t", "--message", dest="message", help="Enter the message")
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
    with open(str(path) + str(filename), "a+") as text:
        text.seek(0)
        # check whether .txt file is either empty or not
        if len(text.read()) > 0:
        # if file is not empty, write the output in next line
            text.write("\n")
        text.write(txt)
    print(style.YELLOW + "[+] Encoded/Decoded message saved in", str(path) + str(filename), style.RESET)


# function to convert string into base64 format

def base64_encode(message, path):
    # convert String to base64
    txt = (base64.b64encode(message.encode("ascii"))).decode("ascii")
    print(style.YELLOW + "[+] Message encoded" + style.RESET)
    # call save_text() to save the encoded message as .txt file
    save_text("Base64en.txt", txt, path)


# function to convert base64 into String format

def base64_decode(message, path):
    # convert base64 into String
    txt = (base64.b64decode(message.encode("ascii"))).decode("ascii")
    print(style.YELLOW + "[+] Message decoded" + style.RESET)
    # call save_text() to save the decoded message as .txt file
    save_text("Base64de.txt", txt, path)


def choice(message, choice, path):
    # If your choose to encode then following block
    if choice == 'Encode' or choice == 'encode' or choice == 'e' or choice == '1':
        base64_encode(message, path)

    # If your choose to decode then following block
    elif choice == 'Decode' or choice == 'decode' or choice == 'd' or choice == '2':
        base64_decode(message, path)
    else:
        print(style.RESET)
        quit()


options = get_argument()
choice(options.message, options.choice, options.path)
