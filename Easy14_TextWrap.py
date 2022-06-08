"""

You are given a string "S" and width "W" .
Your task is to wrap the string into a paragraph of width "W".



"""

import textwrap

string = """ABCDEFGHIJKLIMNOQRSTUVWXYZ"""
max_width = 4


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


result = wrap(string, max_width)
print(result)
