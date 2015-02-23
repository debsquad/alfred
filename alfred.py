#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
import irc.bot

from mods import modpacontent
from mods import modurl
from mods import modzen
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

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(' ', 1)

        if len(a[0]) > 1 and a[0].startswith('!'):
            cmd = a[0][1:].strip().lower()
            self.do_command(e, c, cmd)
        else:
            self.do_listen(e, c)

    def do_listen(self, e, c):
        nick = e.source.nick
        a = e.arguments[0].split(' ', 1)

        try:
            karmacheck = modkarma.listen(a)
            if karmacheck:
                c.privmsg(self.channel, karmacheck)
        except:
            c.notice(nick, 'Error while accessing database.')

        try:
            urlcheck = modurl.parse(nick,e.arguments[0])
            if urlcheck:
                for entry in urlcheck:
                    warnmsg = 'Ce lien a déjà été posté par ' + entry[1]
                    warnmsg += ' le ' + entry[0] + ': ' + entry[2].strip()
                    c.privmsg(self.channel, warnmsg.decode('utf-8'))
        except:
            c.notice(nick, 'Error while accessing url database.')

    def do_command(self, e, c, cmd):
        nick = e.source.nick
        a = e.arguments[0].split(' ', 1)

        if cmd == 'pacontent' and len(a) > 1:
            try:
                c.notice(nick, modpacontent.save(e.arguments[0]))
            except:
                c.notice(nick, "Error while accessing pacontent database")
        elif cmd == 'pacontent' and len(a) == 1:
            try:
                c.privmsg(self.channel, modpacontent.show().decode('utf-8'))
            except:
                c.notice(nick, "Error while accessing pacontent database")
        elif cmd == 'karma' and len(a) > 1:
            try:
                c.privmsg(self.channel, modkarma.show(a))
            except:
                c.notice(nick, "Error while accessing karma database")
        elif cmd == 'zen':
            zencheck = modzen.generate()
            for result in zencheck:
                c.privmsg(self.channel, result)
        elif cmd == 'die':
            if nick == 'vnn':
                self.die()

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
