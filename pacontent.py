import re
import os.path
from random import randint

# Database path
quotesdb = 'quotes.db'
quotes = 0

def init():
    global quotes
    if (not os.path.isfile(quotesdb)):
        print "Unable to access database."
        sys.exit(1)
    else:
        f = open(quotesdb,'r')
        quotes = 0
        for line in f:
            quotes += 1

def process(command,message=None):
    global quotes
    if (command == 'save'):
        rmcmd = re.compile("!pacontent ", re.IGNORECASE)
        message = rmcmd.sub('', message)
        f = open(quotesdb,'a')
        f.write(message + "\n")
        f.close()
        quotes += 1 # increment quotes total in memory
    elif (command == 'show'):
        quote = randint(1, quotes) # random quote line number
        count = 1 # init
        for line in open(quotesdb):
            if (count == quote):
                return str(line)
                break
            count += 1

