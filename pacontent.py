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
        for line in open(quotesdb):
            quotes += 1

def save(message):
    global quotes
    rmcmd = re.compile("!pacontent ", re.IGNORECASE)
    message = rmcmd.sub('', message)
    f = open(quotesdb,'a')
    f.write(message + "\n")
    f.close()
    quotes += 1 # increment quotes total stored in cache

def show():
    global quotes
    quote = randint(1, quotes)
    count = 1
    for line in open(quotesdb):
        if (count == quote):
           return str(line)
           break
        count += 1

