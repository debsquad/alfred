#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import ssl

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

import modpacontent
import modurl
import modkarma

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
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        nick = e.source.nick
        date = time.strftime('%Y-%m-%d %H:%M',time.localtime())

        # module: pacontent
        if re.search("^!Pacontent \w+", e.arguments[0], re.IGNORECASE):
            if (modpacontent.save(e.arguments[0]) != 1):
                c.notice(nick, 'Quote saved.')
            else:
                c.notice(nick, 'Error while accessing database.')
        elif (irc.strings.lower(e.arguments[0]) == '!pacontent'):
            if (modpacontent.show() != 1):
                c.privmsg(self.channel, modpacontent.show().decode('utf-8'))
            else:
                c.notice(nick, 'Error while accessing database.')
        # module: karma
        elif (irc.strings.lower(e.arguments[0]) == '!karma'):
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

        # module: command
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            if (nick == 'vnn'):
                self.do_command(e, a[1].strip())
        return

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
