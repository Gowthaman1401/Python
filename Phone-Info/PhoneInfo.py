#!usr/bin/env python

import optparse, os, subprocess
import phonenumbers                   
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone


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
    parser = optparse.OptionParser(' [-p phonenumber]\n\t[-h help]')
    parser.add_option("-m", "--menu", dest="menu",help="Do you want to return to the Mainmenu(Y/N)?")
    parser.add_option("-p", "--phn", dest="phonenumber", help="Enter phonenumber with county code")
    (options, argument) = parser.parse_args()
    if not options.phonenumber:
        parser.error("Please specify the phone number with county code, Use --help for more info" + style.RESET)
    return options


# function to get details about phonenumber

def num_check(phonenumber):
    try:
        info = []
        number = phonenumbers.parse(phonenumber)
        # to get the carrier service
        info.append(carrier.name_for_number(number, "en"))
        #cto get timezone
        info.append(timezone.time_zones_for_number(number))
        # to get region
        info.append(geocoder.description_for_number(number, "en"))
        return print(style.YELLOW , info , style.RESET)
    except:
        print(style.RED + "[-] Incorrect phonenumber" + style.RESET)


options = get_argument()
num_check(options.phonenumber)
