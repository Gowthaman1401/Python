#!usr/bin/env python

import os
import optparse
import random
import subprocess
import genpasswd as gp

def get_argument():
    parser = optparse.OptionParser(' [-l length] [-i include] [-o wanted_characters] [-n unwanted_characters] [-r repeat_characters(Y/N)] [-h help]')
    parser.add_option("-l", "--length", dest="length", help="Length to the password")
    parser.add_option("-n", "--no", dest="no", help="Unwanted characters to the password")
    parser.add_option("-i", "--include", dest="include", help="Include characters to the password")
    parser.add_option("-o", "--only", dest="only", help="Only wanted characters to the password")
    parser.add_option("-r", "--repeat", dest="repeat", help="Repeat the characters in the password")
    (options, argument) = parser.parse_args()
    return options

def gen_Pass(passlen=False, wanted=False, rep=False, ign=False, inc=False):
	arg = gp.Password(length=passlen, only=wanted, ignore=ign, include=inc, repeat=rep)
	passwd = arg.genPass()
	return print(f"\n{passwd}")

if __name__ == "__main__":
    options = get_argument()
    gen_Pass(options.length, options.only, options.repeat, options.no, options.include)
