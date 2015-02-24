# -*- coding: utf-8 -*-
import os.path
import re
import time

urldb = 'db/urls.db'

def listen(nick, e):
    message = e.arguments[0]
    if re.search('\[nolog\]', message, re.IGNORECASE):
        return None
    message = re.split('\s+', message)
    urlstored = []
    duplicate = []
    registered = False
    urlregex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE | re.UNICODE)

    for word in message:
        if urlregex.match(word):
            if word.endswith('/'):
                word = word[:-1]
            for line in open(urldb):
                line = line.decode('utf-8')
                entry = line.split(' | ')
                if entry[2].strip().lower() == word.lower():
                    duplicate.append(entry)
                    registered = True
            if registered == False:
                urlstored.append(word)

    if urlstored:
        date = time.strftime('%Y-%m-%d %H:%M',time.localtime())
        with open(urldb, 'a') as fp:
            for url in urlstored:
                newline = date + " | " + nick + " | " + url + "\n"
                fp.write(newline.encode('utf-8'))

    if duplicate:
        return duplicate
