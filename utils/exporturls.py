import re
import os

urldb = '/home/vnn/python/alfred/db/urls.db'
for line in open(urldb):
    line = re.split(' \| ', line)
    print '<div>'
    print '<span>' + line[0] + '<span>'
    print '<span>' + line[1] + '<span>'
    print '<a href="' + line[2] + '">' + line[2] + '</a>'
    print '<div>'

