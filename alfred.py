import pyirclib
import string
import sys
import time
import re
import os.path
import pacontent

# config
server = 'irc.oftc.net'
port = 6667
chan = '#alfred'
nickname = 'alfred'
username = 'alfred'
realname = 'Alfred'

# check
pacontent.init()

# connect
irc = pyirclib.Irclib(server,port)
irc.setDebug = 1
irc.login(nickname,username=username,realname=realname)
irc.join(chan)

# parser
def parsemessage(msg):
    if msg['event'] == "PRIVMSG": # msg inside chan
        message = str(msg['text']).replace('\r','')

        # FEATURE: Pacontent
        if re.search("^!Pacontent \w+", message, re.IGNORECASE):
            pacontent.save(message)
        elif re.search("^!Pacontent$", message, re.IGNORECASE):
            irc.privmsg(chan,pacontent.show())

while 1:
  message = irc.getmessage()
  print message
  parsemessage(message)

