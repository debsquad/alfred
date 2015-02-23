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

    is_newuser = 1
    user = a[0][:-2].encode('utf-8')
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
            is_newuser = 0
        dest.write(line)

    source.close()
    dest.close()
    os.remove(karmadb+"~")

    if is_newuser == 1:
        if a[0].endswith('++'):
            total = 1
        else:
            total = -1
        with open(karmadb, 'a') as fp:
            fp.write(user + ':' + str(total) + '\n')

    return 'Le karma de ' + user.decode('utf-8') + ' est de: ' + str(total)

def show(e):
    a = e.arguments[0].split(' ', 1)
    if len(a) <= 1:
        return False
    user = a[1].split(' ', 1)
    user = user[0].encode('utf-8')
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
        return 'Le karma de ' + user.decode('utf-8') + ' est de: ' + str(total)
