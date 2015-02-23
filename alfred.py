#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import ssl
import irc.bot

from mods import modpacontent
from mods import modurl
from mods import modzen
from mods import modkarma

class alfred(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6697):
        factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(server, port)],
            nickname,
            nickname,
            connect_factory = factory)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)
        helloworld = [ 'y0', 'wesh', 'salut', 'moo', 'm00', 'salutations' ]
        r = random.randint(0,len(helloworld)-1)
        c.privmsg(self.channel, helloworld[r])

    def on_pubmsg(self, c, e):
        e.arguments[0] = e.arguments[0].encode('utf-8')
        a = e.arguments[0].split(' ', 1)
        if len(a[0]) > 1 and a[0].startswith('!'):
            self.do_command(e, c)
        else:
            self.do_listen(e, c)

    def irc_output(self, output):
        return output.decode('utf-8')

    def do_listen(self, e, c):
        nick = e.source.nick

        # modKarma
        try:
            karmacheck = modkarma.listen(e)
            if karmacheck:
                c.privmsg(self.channel, self.irc_output(karmacheck))
                return
        except:
            c.notice(nick, 'Error while accessing database.')

        # modUrl
        urlcheck = modurl.listen(nick, e)
        if urlcheck:
            for entry in urlcheck:
                warnmsg = 'Ce lien a déjà été posté par ' + entry[1]
                warnmsg += ' le ' + entry[0] + ': ' + entry[2].strip()
                c.privmsg(self.channel, self.irc_output(warnmsg))
            return

    def do_command(self, e, c):
        nick = e.source.nick
        a = e.arguments[0].split(' ', 1)
        cmd = a[0][1:].strip().lower()

        if cmd == 'pacontent':
            try:
                c.privmsg(self.channel, self.irc_output(modpacontent.process(e)))
            except:
                c.notice(nick, "Error while accessing pacontent database")
        elif cmd == 'karma':
            try:
                c.privmsg(self.channel, self.irc_output(modkarma.show(e)))
            except:
                c.notice(nick, "Error while accessing karma database")
        elif cmd == 'zen':
            zencheck = modzen.generate()
            for result in zencheck:
                c.privmsg(self.channel, result)
        elif cmd == 'die':
            if nick == 'vnn':
                self.die()
        elif cmd == 'disconnect':
            if nick == 'vnn':
                self.disconnect()

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
