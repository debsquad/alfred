import pyirclib
import string
import sys
import time
import re
import os.path
from random import randint

# configuration
quotesdb = 'quotes.db'
server = 'irc.oftc.net'
port = 6667
chan = '#debsquad'

# connexion
irc = pyirclib.Irclib(server,port)
irc.setDebug = 1
irc.login('alfred',username = 'alfred')
irc.join(chan)

# parser
def parsemessage(msg):
    if msg['event'] == "PRIVMSG": # if msg in channel
        message = str(msg['text']).replace('\r','') # we store/format it

        # FEATURE: Pacontent
        if re.search("^!Pacontent", message, re.IGNORECASE):
            # check for database
            if (not os.path.isfile(quotesdb)):
                irc.privmsg(chan,"Unable to access database.")
            # save entry
            elif re.search("^!Pacontent \w+", message, re.IGNORECASE):
                rmcmd = re.compile("!pacontent ", re.IGNORECASE)
                message = rmcmd.sub('', message)
                f = open(quotesdb,'a')
                f.write(message + "\n")
                f.close()
            # show random entry
            elif re.search("^!Pacontent$", message, re.IGNORECASE):
                quotes = 0 # init
                f = open(quotesdb,'r')
                for line in f:
                    quotes += 1
                quote = randint(1, quotes) # random quote line number
                count = 1 # init
                for line in f:
                    if (count == quote):
                        formatline = str(line)
                        irc.privmsg(chan,formatline)
                    count += 1

# enable real time parsing
while 1:
  message = irc.getmessage()
  print message
  parsemessage(message)

