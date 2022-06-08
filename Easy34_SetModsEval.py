"""
Task

You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer N, the number of elements in the set s.
The second line contains n space separated elements of set s. 
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
"""

# first line receives an integer corresponding to the number of elements in the set
# Not really necessary, could simply populate the set and then count the length
n = int(input())

# populate the set and ensure the values are set as integers
mySet = set(map(int, input().split()))

# Enter the loop for a specific number of iterations based on the third line of input
# Could be done with i = input(), but will use a comprehension format
for i in range(int(input())):
    # eval() validate and executes and expression.
    # eval() allows the use of variables or structures to build expressions
    eval('mySet.{0}({1})'.format(*input().split()+[' ']))
    print(mySet)
    print(sum(mySet))




