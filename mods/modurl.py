# -*- coding: utf-8 -*-
import os.path
import re
import time

urldb = 'db/urls.db'

def listen(nick, e):
    message = e.arguments[0]
    message = re.split('\s+', message)
    urlstored = []
    duplicate = []
    urlregex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE | re.UNICODE)

    for word in message:
        if urlregex.match(word):
            # format url
            if word.endswith('/'):
                word = word[:-1]
            newurl = 1
            for line in open(urldb):
                entry = line.split(' | ')
                if entry[2].strip().lower() == word.lower():
                    newurl = 0
                    duplicate.append(entry)
            if newurl == 1:
                urlstored.append(word)

    if urlstored:
        date = time.strftime('%Y-%m-%d %H:%M',time.localtime())
        with open(urldb, 'a') as fp:
            for url in urlstored:
                fp.write(date + " | " + nick + " | " + url + "\n")

    if duplicate:
        return duplicate
