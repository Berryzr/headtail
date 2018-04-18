import random
import sys
import os

#introduction
print "HEADS OR TAILS"
print """\nEnter [f] to flip the coin
Enter [q] to quit
__________________________"""

def restart_program():
    "restarts the current program to the beginning"
    python = sys.executable
    os.execl(python, python, * sys.argv)

#This is the list of both possible coin outcomes
coin = ['Heads', 'Tails']

activate = raw_input()

#This is the output section
if activate == 'f':
    os.system('clear')
    print (random.choice(coin))

#How to quit function
elif activate == 'q':
    sys.exit()

else:
    print 'Invalid response'

#retry function
print "\nRetry? (y/n)"
answer = raw_input()
#y plays again (retry)
if answer == 'y':
    os.system("printf '\033c'")
    restart_program()
#n leaves the system
elif answer == 'n':
    print "See you later"
    sys.exit()
