"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
The re module offers a set of functions that allows us to search a string for a match:
https://www.youtube.com/watch?v=WQlKPdKVXfw
"""

import re

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))