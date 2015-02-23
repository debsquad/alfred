# alfred
Alfred is a simple ircbot using SSL.

## Requirements
 * Python 2.7: https://www.python.org/
 * Package IRC: https://pypi.python.org/pypi/irc

## Usage
alfred \<server[:port]\> \<channel\> \<nickname\>

## Modules
Here are the available modules:
 * **modPacontent**:
   * _''!pacontent \<quote\>``_ saves the specified quote in a text database.
   * _''!pacontent``_ randomly output one of the database entries.
 * **modUrl**: silently stores channel urls into a text database.
   If a link was previously stored, print a message with information from database.
 * **modKarma**: increments user's karma with _''\<nickname\>++``_. You can also print 
   one user's karma with _''!karma \<nicname\>``_.
 * **modZen**: prints random part of "import this" by Tim Peters
