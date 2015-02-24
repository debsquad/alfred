# -*- coding: utf-8 -*-
import os.path
import random

quotesdb = 'db/pacontent.db'

def process(e):
    a = e.arguments[0].split(' ', 1)

    # save
    if len(a) > 1:
        msg = a[1].encode('utf-8')
        with open(quotesdb, 'a') as fp:
            fp.write(msg + "\n")
        return "Quote saved."

    # show
    with open(quotesdb) as fp:
        quotes = fp.readlines()
        if quotes:
            quote = random.choice(quotes).strip()
            return quote.decode('utf-8')
        return "Database is empty"
