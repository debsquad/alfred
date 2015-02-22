#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import ssl

import irc.bot

from mods import modpacontent
from mods import modurl
from mods import modkarma

class alfred(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6697):
        factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname, connect_factory = factory)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)
        c.privmsg(self.channel, "y0")

    def on_privmsg(self, c, e):
        if (e.arguments[0].lower() == '!die'):
            if (nick != 'vnn'):
                self.die()

    def on_pubmsg(self, c, e):
        nick = e.source.nick
        date = time.strftime('%Y-%m-%d %H:%M',time.localtime())

        # module: pacontent
        if re.search("^!Pacontent \w+", e.arguments[0], re.IGNORECASE):
            if (modpacontent.save(e.arguments[0]) != 1):
                c.notice(nick, 'Quote saved.')
            else:
                c.notice(nick, 'Error while accessing database.')
        elif (e.arguments[0].lower() == '!pacontent'):
            if (modpacontent.show() != 1):
                c.privmsg(self.channel, modpacontent.show().decode('utf-8'))
            else:
                c.notice(nick, 'Error while accessing database.')
        # module: karma
        elif (e.arguments[0].lower() == '!karma'):
            c.privmsg(self.channel, modkarma.generate())
        # module: url
        else:
            urlcheck = modurl.parse(date,nick,e.arguments[0])
            if (urlcheck):
                if (urlcheck == 1):
                    c.notice(nick, 'Error while accessing database.')
                else:
                    for entry in urlcheck:
                        warnmsg = "Ce lien a déjà été posté par " + entry[1]
                        warnmsg += ' le ' + entry[0] + ': ' + entry[2].strip()
                        c.privmsg(self.channel, warnmsg.decode('utf-8'))
        return

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: alfred <server[:port]> <channel> <nickname>")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6697
    channel = sys.argv[2]
    nickname = sys.argv[3]

    bot = alfred(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
