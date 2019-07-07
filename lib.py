#-*-coding: utf-8-*-
from time import strftime

getDate = lambda: "{}-{}".format(strftime("%d-%m-%y"),strftime("%H-%M-%S"))

def banner():
	print('''
      Attacker /_______________  |    |
	O|====| _______________/ | sp |  You
	       \\                 |    |

	    [+]By Binario
	    [+]Github:https://github.com/binarioGH
		''')