"""
"Double Ended Que"
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same
performance in either direction.

Task

Perform append, pop, popleft and appendleft methods on an empty deque d.
functions as list, but allows methods to the left of the list.

https://www.youtube.com/watch?v=m3JgSV1Obn8
"""

from collections import deque

d = deque("")

for i in range(int(input())):
    # populate the deque
    # eval() validate and executes and expression.
    # eval() allows the use of variables or structures to build expressions
    eval('d.{0}({1})'.format(*input().split()+[' ']))

    
for i in range(len(d)):
    print(d[i], end=" ")