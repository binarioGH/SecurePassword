#-*-coding: utf-8-*-
from random import randint
from optparse import OptionParser as opt
from sys import argv
from lib import *
import codecs


def getsPass(l,bannedchars="",spaces=True):
	if not spaces:
		bannedchars += " "
	password = ""
	while len(password) != l:
		char = chr(randint(32,254))
		if char in bannedchars:
			continue
		else:
			password += char
	return password


def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-l", "--lenght", dest="len", default=16, type="int", help="Set password's lenght.")
	op.add_option("-b", "--bannedchars", dest="bnd", default="", help="Set what characters you don't want to have in your password.")
	op.add_option("-d", "--disablespaces",action="store_false",dest="spaces", default=True,help="Use this flag if you do not want spaces in your secure password.")
	op.add_option("-s", "--store", action="store_true", dest="store", default=False, help="Store your passwore in a file.")
	op.add_option("-n", "--storefilename", dest="sname", default="spass{}.txt".format(getDate()), help="Defina a file name.")
	op.add_option("-p", "--donotprint", dest="print", action="store_false", default=True, help="Use this flag if you don't want to print your result.")
	(o, argv) = op.parse_args()
	spass = getsPass(o.len, bannedchars=o.bnd, spaces=o.spaces)
	if o.print:
		print("Your new password: {}".format(spass))
	if o.store:
		try:
			with codecs.open(o.sname, "w", encoding="utf-8") as f:
				f.write(spass)
		except Exception as e:
			print(e)



if __name__ == '__main__':
	banner()
	main()