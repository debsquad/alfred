# -*- coding: utf-8 -*-
import os
import re

karmadb = 'db/karma.db'

def listen(e):
    a = e.arguments[0].split(' ', 1)
    if len(a) != 1:
        return None
    a[0] = a[0].strip()
    if not a[0].endswith('++') and not a[0].endswith('--'):
        return None
    if len(a[0]) < 3:
        return None
    if a[0][:-2] == 'all':
        return None

    user = a[0][:-2]
    os.rename(karmadb, karmadb+"~" )
    dest = open(karmadb, 'w')
    source = open(karmadb+'~', 'r')

    for line in source:
        if re.search(re.escape(user), line, re.IGNORECASE):
            line = line.strip().split(':')
            if a[0].endswith('++'):
                total = int(line[1]) + 1
            else:
                total = int(line[1]) - 1
            line = user + ':' + str(total) + '\n'
            registered= 1
        dest.write(line.encode('utf-8'))

    source.close()
    dest.close()
    os.remove(karmadb+"~")

    if not registered:
        if a[0].endswith('++'):
            total = 1
        else:
            total = -1
        with open(karmadb, 'a') as fp:
            line = user + ':' + str(total) + '\n'
            fp.write(line.encode('utf-8'))

    return 'Le karma de ' + user + ' est de: ' + str(total)

def show(e):
    a = e.arguments[0].split(' ', 1)
    if len(a) <= 1:
        return False
    user = a[1].split(' ', 1)
    user = user[0]
    total = 0
    allentries = ''

    for line in open(karmadb):
        if user == 'all':
            allentries += line.strip() + ' | '
        else:
            if re.search(re.escape(user), line, re.IGNORECASE):
                line = line.strip().split(':')
                total = line[1]
                break

    if user == 'all':
        if allentries:
            return allentries[:-3].decode('utf-8')
        else:
            return "Database is empty"
    else:
        return 'Le karma de ' + user + ' est de: ' + str(total)
