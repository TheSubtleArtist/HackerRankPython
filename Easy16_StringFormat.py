"""
Given an integer, n, print the following values for each integer i from 1 to n :
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

https://www.python.org/dev/peps/pep-3101/
https://realpython.com/python-formatted-output/

"""

n = 4
print()

for i in range(1, n+1):
	#width = len("{0:b}".format(n))
	print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=len("{0:b}".format(n))))

"""
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two')) # 0 and 1 are positional to the strings sent to the function
print('{:>10}'.format('test')) #forces right justification of the string using 10 spaces
print('{:10}'.format('test')) #prints the string 'test' using 10 spaces, leaving 6 spaces after the last letter
print('{:_<10}'.format('test')) #left justified, 10 spaces, '_' as space filler
print('{:_^10}'.format('test')) #center justified, 10 spaces, '_' as space filler
print('{:_^9}'.format('test')) #center justified,  spaces, '_' as space filler, uneven distribution is placed to the right
print('{:.5}'.format('crazylongwords')) #truncates to only the first 5 characters (the number following the period)
print('{:10.5}'.format('crazylongwords')) #10 spaces, but only the first 5 characters
"""
"""
#Numbers
print('{:d}'.format(42)) #formats to decimal
print('{:4d}'.format(42)) #formats to decimal with four padding spaces, right justify
print('{:f}'.format(42)) #formats to float
print('{:06.2f}'.format(3.141592653589793)) #'0' is the padding character, total 6 space, 2 spaces after the
print('{:+d}'.format(42)) #forces the sign
print('{: d}'.format(-42)) #leading space before the negative number
print('{: d}'.format(42)) #leading space aligns
print('{:=5d}'.format(42)) #leading space aligns
print('{:=+5d}'.format(42)) #'=' controls the position of the '+' sign over 5 spaces

"""