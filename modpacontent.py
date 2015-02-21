# -*- coding: utf-8 -*-
import re
import os.path
import random

quotesdb = 'db/pacontent.db'

def checkdb():
    if (not os.path.isfile(quotesdb)):
        if (open(quotesdb, 'w').close()):
            pass
        else:
            return 1

def save(message):
    if (checkdb() != 1):
        rmcmd = re.compile("!pacontent ", re.IGNORECASE)
        message = rmcmd.sub('', message).encode('UTF-8')
        f = open(quotesdb,'a')
        f.write(message + "\n")
        f.close()
    else:
        return 1

def show():
    if (checkdb() != 1):
        with open(quotesdb) as fp:
            quotes = fp.readlines()
            if (quotes):
                quote = random.choice(quotes)
                quote = quote.replace('\n','').replace('\r','')
                return quote
            else:
                return "Database is empty"
    else:
        return 1

