import pyirclib
import string
import sys
import time
import re
import os.path
import pacontent

server = 'irc.oftc.net'
port = 6667
chan = '#alfred'

pacontent.init()

irc = pyirclib.Irclib(server,port)
irc.setDebug = 1
irc.login('alfred',username = 'alfred')
irc.join(chan)

# parser
def parsemessage(msg):
    if msg['event'] == "PRIVMSG": # if msg in channel
        message = str(msg['text']).replace('\r','') # we store/format it

        # FEATURE: Pacontent
        if re.search("^!Pacontent \w+", message, re.IGNORECASE):
            pacontent.process('save', message)
        # show random entry
        elif re.search("^!Pacontent$", message, re.IGNORECASE):
            irc.privmsg(chan,pacontent.process('show'))

# enable real time parsing
while 1:
  message = irc.getmessage()
  print message
  parsemessage(message)

