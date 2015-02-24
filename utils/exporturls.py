import re
import os

urldb = '../db/urls.db'

print """
<!doctype html>
<html lang="">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400' rel='stylesheet' type='text/css'>
        <style>
        .clearfix:before,
        .clearfix:after {
            content: " ";
            display: table;
        }
        .clearfix:after { clear: both; }
        a, a:visited {
            color: #666;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
            color: #333;
        }
        body {
            padding: 3em;
            line-height: 1.6;
            font-family: 'Open Sans', sans-serif;
            background: #e8e8e8;
            color: #444;
            font-weight: 300;
        }
        .wrap {
            width: 100%;
            max-width: 1140px;
            margin: 0 auto;
            background: white;
            padding: 2em 2em 3em;
            box-sizing: border-box;
        }
        .entry {background: white;border-radius: 2px; overflow: hidden;}
        .var { background: #f8f8f8;}
        table { border: none; }
        td { padding: .6em 1em; vertical-align: top;}
        td:first-of-type { min-width: 9em }
        td:last-of-type { color: #444 }
        </style>
    </head>
    <body>
        <div class=wrap>
        <table cellspacing="0" cellpadding="0">
"""

urlpack = []
for line in open(urldb):
    urlpack.append(line)

count = 0
urlpack.reverse()
for line in urlpack:
    line = re.split(' \| ', line)
    if count == 0:
        print '<tr class="entry clearfix">'
    else:
        print '<tr class="entry var clearfix">'
    print '    <td>' + line[0] + '</td>'
    print '    <td>' + line[1] + '</td>'
    print '    <td><a href="' + line[2] + '">' + line[2] + '</a></td>'
    print '</tr>'
    count += 1
    if count == 2:
        count = 0

print """
        </table>
        </div>
    </body>
</html>
"""
