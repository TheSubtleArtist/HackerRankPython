"""You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements: 
-Number can start with +, - or . symbol.
-Number must contain at least decimal value.
-Number must have exactly one . symbol. 
-Number must not give any exceptions when converted using float(n).
"""




import re

for i in range(int(input())):
    print(bool(re.match('^[-+]?[0-9]*\.[0-9]+$', input())))

    # ^[+-]? : indicates the string must begin with zero or one occurances of either + or -
    # [0-9]* : indicates the string may contain zero or more numbers from the set of numbers 0-9
    # \*. : indicates there must be exactly one occurance of the "."
    # [0-9]+$ : indicates the string must end with ($) 1 or more (+) occurances of the numbers 0-9