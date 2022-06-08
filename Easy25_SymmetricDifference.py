"""
Objective
Today, we're learning about a new data type: sets.

Concept
If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list.
The delimiter is space (ascii 32) by default.
To specify that comma is the delimiter, use string.split(',').
For this challenge, and in general on HackerRank, space will be the delimiter.

Task:
Given sets of integers, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either or but do not exist in both.

"""
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))

