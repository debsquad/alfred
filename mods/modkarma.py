# -*- coding: utf-8 -*-
import os
import re

karmadb = 'db/karma.db'

def listen(a):
    if len(a) != 1:
        return None
    a[0] = a[0].strip()
    if not a[0].endswith('++'):
        return None
    if len(a[0]) < 3:
        return None

    isnewuser = 1
    user = a[0][:-2].encode('utf-8')
    os.rename(karmadb, karmadb+"~" )
    dest = open(karmadb, 'w')
    source = open(karmadb+'~', 'r')

    for line in source:
        if re.search(re.escape(user), line, re.IGNORECASE):
            line = line.strip().split(':')
            total = int(line[1]) + 1
            line = user + ':' + str(total) + '\n'
            isnewuser = 0
        dest.write(line)

    source.close()
    dest.close()
    os.remove(karmadb+"~")

    if isnewuser == 1:
        total = 1
        with open(karmadb, 'a') as fp:
            fp.write(user + ':1\n')

    return 'Le karma de ' + user.decode('utf-8') + ' est de: ' + str(total)

def show(a):
    user = a[1]
    user = user.split(' ', 1)
    user = user[0].encode('utf-8')
    source = open(karmadb)
    total = 0

    for line in source:
        if re.search(re.escape(user), line, re.IGNORECASE):
            line = line.strip().split(':')
            total = line[1]
            break

    return 'Le karma de ' + user.decode('utf-8') + ' est de: ' + str(total)
