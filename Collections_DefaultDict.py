"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

#For Example:

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)

Task:
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each m occurrence of in group A.
If it does not appear, print -1 .
"""
from collections import defaultdict

d = defaultdict(list)
list1=[]

#n, m = map(int, input().split())

n=5
m = 2

for i in range(0,n):
    d[input('inA')].append(i+1)
    print(d)

for i in range(0,m):
    list1=list1+[input('inB')]
    print(list1)

for i in list1:
    if i in d:
        print(" ".join( map(str,d[i]) ))
    else:
        print(-1)