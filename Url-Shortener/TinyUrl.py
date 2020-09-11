#!usr/bin/env python

import os, subprocess, optparse
import pyshorteners                      


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
    parser = optparse.OptionParser(' [-u url] [-h help]')
    parser.add_option("-u", "--url", dest="url", help="Enter the URL" + style.RESET)
    (options, argument) = parser.parse_args()
    if not options.url:
        parser.error("Please specify the URL, Use --help for more info" + style.RESET)
    return options


# function helps to shorten URL

def shorten(url):
    link = pyshorteners.Shortener()
    return print(style.YELLOW + "[+] Original url : " + url + "\n[+] Shorten url : " + link.tinyurl.short(url),  style.RESET)


options = get_argument()
shorten(options.url)
