# Want to use PyTools? Put this file in the same folder as another Python file,
# then at the top of the other file put "import pytools". Enjoy!
import random


# getEscCode(key) returns an ANSI escape code in the form of a string by a key.
# Some examples of keys include "bold", "highlightColor-blue", or "clear".
# To use ANSI escape codes, concatenate this function to the start of a string.
# To end the effect, concatenate this function to the point in a string where the effects should be cleared,
# but either provide the key "clear" or do not provide a key at all.
def getEscCode(key='clear'):
  keys = key.split('-')
  escCodes = {
      'bold': '1',
      'italic': '3',
      'underline': '4',
      'textColor': '38;5;',
      'highlightColor': '48;5;',
      'clear': '0',
  }
  colorEscCodes = {
      'black': '0',
      'grey': '8',
      'white': '15',
      'red': '9',
      'green': '10',
      'yellow': '11',
      'blue': '12',
      'magenta': '13',
      'cyan': '14',
  }

  escCode = escCodes.get(keys[0])
  if len(keys) > 1:
    escCode = str(escCode) + str(colorEscCodes.get(keys[1]))
  return '\033[' + str(escCode) + 'm'

# seperateBigNum(number) returns the same number, with commas applied after every third digit.
# For example, seperateBigNum(124727421) returns "124,727,421".
def separateBigNum(number):
  output = ''
  digits = []
  for x in number:
    digits += [x]
  digits.reverse()

  for x in digits:
    output = x + output
    if len(output) % 4 == 3:
      output = ',' + output

  output = output.lstrip(',')

  return output
