#!/usr/bin/python

import base64
import sys
import getopt

def usage():
	print "\n\n   ____ ___ ___  ___  _____________ _________  __  ___"
	print "  / __/|_  ( _ )/ _ \/ __/ __/ ___// ___/ __ \/  |/  /"
	print " /__ \/ __/ _  / // /\ \/ _// /___/ /__/ /_/ / /|_/ / "
	print "/____/____|___/\___/___/___/\___(_)___/\____/_/  /_/  \n"
	
	print "~ b32.py is a simple python script to perform base32 encoding/decoding on strings. ~"
	print "~ Coded by @ndrwsvk                                                                ~"
	print "~ 5280sec.com                                                                      ~"
	print "~                                                                                  ~"
	print "~ This work is licensed under a Creative Commons Attribution-NonCommercial-        ~"
	print "~ ShareAlike 4.0 International License:                                            ~"
	print "~ http://creativecommons.org/licenses/by-nc-sa/4.0/                                ~"
	print "~                                                                                  ~"
	print "~ Usage:                                                                           ~"
	print '~ Encode a string: ./b32.py -e -s "This is the string to encode."                  ~'
	print '~ Decode a string: ./b32.py -d -s JZXXI2DJNZTSA5DPEBZWKZJANBSXEZJOFYXA====         ~'
	print '\n\n'
	sys.exit()
	
def start(argv):
	try:
		options, args = getopt.getopt(argv, "des:")
	except getopt.GetoptError, e:
		print "An error occurred: "+e
		sys.exit()

	for opt, arg in options:
		if opt == '-d':
			op = "decoded"
		if opt == '-e':
			op = "encoded"	
		if opt == '-s':
			string = arg

	if op == "decoded" and string[-1:] != "=":
		string += "="

	if op == "decoded":
		try:
			output = base64.b32decode(string.upper())
		except Exception, e:
			print "An error occurred: "+e
			sys.exit()

	if op == "encoded":
		try:
			output = base64.b32encode(string)
		except Exception, e:
			print "An error occurred: "+e
			sys.exit()

	print "Your string has been "+op+":"
	print output

 

if __name__ == "__main__":
    try:
	if len(sys.argv) < 4:
		usage()
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Operation interrupted by user..."
    except:
        sys.exit()
