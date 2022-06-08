"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

line = 'this is a string'

def split_and_join(line):
	lineList = line.split()
	newLine = '-'.join(lineList)
	return newLine

print(line)
result = split_and_join(line)
print(result)