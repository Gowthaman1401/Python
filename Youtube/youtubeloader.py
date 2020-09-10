#!usr/bin/env python

import os, optparse, subprocess
import webbrowser


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
    parser = optparse.OptionParser(' [-u url] [-c choice]\n\t[-h help]')
    parser.add_option("-u", "--url", dest="url",help="Url to youtube video (url should be in https://www.youtube.com/..... format)")
    parser.add_option("-c", "--choice", dest="choice",help="Enter your choice (1.DownloadVideo / 2.DownloadSubtitle(if available) / 3.WatchWithoutAds / 4.WatchAgeRestricted")
    (options, argument) = parser.parse_args()
    if not options.url and not options.choice:
        parser.error(style.RED+ "Please specify the Url to youtube video and your choice, Use --help for more info" + style.RESET)
    if not options.url:
        parser.error(style.RED+ "Please specify the Url to youtube video, Use --help for more info" + style.RESET)
    if not options.choice:
        parser.error(style.RED+ "Please enter your choice, Use --help for more info" + style.RESET)
    return options


# function which redirects to dowmload page in default browser

def utube(url, choice):
    try:
        sub = url[:8] + 'subtitle.to/' + url[0:]
        down = url[:12] + 'ss' + url[12:]
        ads = url[:23] + '.' + url[23:]
        age = url[:12] + 'nsfw' + url[12:]
        if choice == '1' or choice == 'DownloadVideo':
            webbrowser.open(down)
        elif choice == '2' or choice == 'DownloadSubtitle':
            webbrowser.open(sub)
        elif choice == '3' or choice == 'WatchWithoutAds':
            webbrowser.open(ads)
        elif choice == '4' or choice == 'WatchAgeRestricted':
            webbrowser.open(age)
        print(style.YELLOW + "[-] You have to do it manually!" + style.RESET)
    except:
        print(style.RED+ "[-] Invalid url" + style.RESET)


options = get_argument()
utube(options.url, options.choice)
