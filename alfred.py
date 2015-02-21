#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

import pacontent

class alfred(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    # if nickname is used
    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    # once connected to the server
    def on_welcome(self, c, e):
        c.join(self.channel)
        c.privmsg(self.channel, "y0")

    # on private message
    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    # on public message
    def on_pubmsg(self, c, e):
        nick = e.source.nick
        if re.search("^!Pacontent \w+", e.arguments[0], re.IGNORECASE):
            if (pacontent.save(e.arguments[0]) != 1):
                c.notice(nick, 'Quote saved.')
            else:
                c.notice(nick, 'Error while accessing database.')
        elif (irc.strings.lower(e.arguments[0]) == '!pacontent'):
            c.privmsg(self.channel, pacontent.show().decode('utf-8'))

        # talkinkg to the bot
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            self.do_command(e, a[1].strip())
        return

    # command definitions
    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        if cmd == "disconnect":
            self.disconnect()
        elif cmd == "die":
            self.die()
        elif cmd == "stats":
            for chname, chobj in self.channels.items():
                c.notice(nick, "--- Channel statistics ---")
                c.notice(nick, "Channel: " + chname)
                users = chobj.users()
                users.sort()
                c.notice(nick, "Users: " + ", ".join(users))
                opers = chobj.opers()
                opers.sort()
                c.notice(nick, "Opers: " + ", ".join(opers))
                voiced = chobj.voiced()
                voiced.sort()
                c.notice(nick, "Voiced: " + ", ".join(voiced))
        else:
            c.notice(nick, "Not understood: " + cmd)

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: testbot <server[:port]> <channel> <nickname>")
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
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    bot = alfred(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
