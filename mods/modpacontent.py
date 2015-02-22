# -*- coding: utf-8 -*-
import re
import os.path
import random

quotesdb = 'db/pacontent.db'

def save(message):
    cmdregex = re.compile("!pacontent ", re.IGNORECASE)
    message = cmdregex.sub('', message).encode('UTF-8')
    with open(quotesdb, 'a') as fp:
        fp.write(message + "\n")
    return "Quote saved."

def show():
    with open(quotesdb) as fp:
        quotes = fp.readlines()
        if quotes:
            quote = random.choice(quotes).strip()
            return quote
        else:
            return "Database is empty"

