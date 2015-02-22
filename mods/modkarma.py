# -*- coding: utf-8 -*-
import os
import re

karmadb = 'db/karma.db'

def checkdb():
    if not os.path.isfile(karmadb):
        if open(karmadb, 'w'):
            pass
        else:
            return 1

def listen(a):
    a[0] = a[0].strip()

    if checkdb() != 1:
        if len(a) == 1 and a[0].endswith('++'):
            isnewuser = 1
            user = a[0][:-2]

            os.rename(karmadb, karmadb+"~" )
            dest = open(karmadb, 'w')
            source = open(karmadb+'~', 'r')
            for line in source:
                if re.search(re.escape(user), line, re.IGNORECASE):
                    line = line.strip().split(':')
                    total = int(line[1]) + 1
                    line = user + ':' + str(total)
                    isnewuser = 0
                dest.write(line)
            source.close()
            dest.close()
            os.remove(karmadb+"~")

            if isnewuser == 1:
                total = 1
                with open(karmadb, 'a') as fp:
                    fp.write(user + ':1')

            return 'Le karma de ' + user + ' est de: ' + str(total)
    else:
        return 1

def show(a):
    if checkdb() != 1:
        if len(a) > 1:
            user = a[1]
            user = user.split(' ', 1)
            user = user[0]
            source = open(karmadb)
            total = 0
            for line in source:
                if re.search(re.escape(user), line, re.IGNORECASE):
                    line = line.strip().split(':')
                    total = line[1]
                    break
            return 'Le karma de ' + user + ' est de: ' + str(total)
        else:
            return 'Arg is missing.'
    else:
        return "Error while accessing database."

