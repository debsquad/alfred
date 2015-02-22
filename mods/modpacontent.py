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
        cmdregex = re.compile("!pacontent ", re.IGNORECASE)
        message = cmdregex.sub('', message).encode('UTF-8')
        with open(quotesdb, 'a') as fp:
            fp.write(message + "\n")
    else:
        return 1

def show():
    if (checkdb() != 1):
        with open(quotesdb) as fp:
            quotes = fp.readlines()
            if (quotes):
                quote = random.choice(quotes).strip()
                return quote
            else:
                return "Database is empty"
    else:
        return 1

