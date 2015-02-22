# -*- coding: utf-8 -*-
import os.path
import re

urldb = 'db/urls.db'

def checkdb():
    if (not os.path.isfile(urldb)):
        if (open(urldb, 'w').close()):
            pass
        else:
            return 1

def parse(date, nick, message):
    if (checkdb() != 1):
        message = re.split('\s+', message)
        urlstored = []
        duplicate = []
        urlformat = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        schemeformat = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)

        for word in message:
            if (urlformat.match(word)):
                # format url
                if not schemeformat.match(word):
                    word = 'http://' + word
                if word.endswith('/'):
                    word = word[:-1]
                newurl = 1
                for line in open(urldb):
                    entry = re.split(' \| ', line)
                    if (entry[2].strip().lower() == word.lower()): # url already saved
                        newurl = 0
                        duplicate.append(entry)
                if (newurl == 1):
                    urlstored.append(word)

        if urlstored:
            f = open(urldb, 'a')
            for url in urlstored:
                f.write(date + " | " + nick + " | " + url + "\n")
            f.close()

        if duplicate:
            return duplicate
