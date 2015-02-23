# alfred
alfred is a simple ircbot using SSL.

## Requirements
 * Python 2.7: https://www.python.org/
 * Package IRC: https://pypi.python.org/pypi/irc

## Usage
alfred \<server[:port]\> \<channel\> \<nickname\>

## Modules
Here are the available modules:
 * **modPacontent**:
   * _!pacontent \<quote\>_: saves the specified quote in a text database.
   * _!pacontent_: randomly output one of the database entries.
 * **modKarma**:
   * _\<nickname\>++_: increments user karma
   * _!karma \<nicname\>_: prints user karma
 * **modZen**:
   * _!zen_: prints random part of "import this" by Tim Peters
 * **modUrl**: silently stores channel urls into a text database.
   If a link was previously stored, print a message with information from database.
