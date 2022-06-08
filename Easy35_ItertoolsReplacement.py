"""
itertools.combinations_with_replacement(iterable, r)
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task

You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string
and integer value separated by a space.
"""

from itertools import combinations_with_replacement

strng, size = input().split()
strng = strng.upper()
strng = list(strng)
print(strng)
print(size)
"""
This actually didn't work, it missed the letter "h". no idea why
newList = sorted(list(combi(strng, int(size))))

for i in newList:
    print("".join(i))
"""

for i in combinations_with_replacement(sorted(strng), int(size)):
    print("".join(i))