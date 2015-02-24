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
   * _!pacontent \<quote\>_: save the specified quote in a text database
   * _!pacontent_: randomly output one of the database entries
 * **modKarma**:
   * _\<nickname\>--_: decrement nickname karma
   * _\<nickname\>++_: increment nickname karma
   * _!karma \<nicname\>_: print nickname karma
   * _!karma all_: print all database entries
 * **modZen**:
   * _!zen_: print random part of "import this" by Tim Peters
 * **modUrl**: 
   * silently store channel urls into a text database.
   * print a warning if an url was already recorded
   * feature _utils/exporturls.py_ to generate a simple web page from 
     database
