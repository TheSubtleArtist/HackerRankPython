"""
There is a horizonal ros of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should vollow these directions:

if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i]

When stacking the cubes, you can only pick up either the leftmost or the right most cube each time
Print "yes" if it is possible to stack the cubes, otherwise print "No"

Input format:
First line: "T" is the number of test cases
Each test case requires two lines
first line of each test case contains n, the number of blocks
second line of each test case contains n number of blocks

"""

from collections import deque


def stack(listSize, theList):
    blocks = theList
    x = float('inf')
    while blocks:
        mySpot = blocks.popleft() if blocks[0]>blocks[-1] else blocks.pop() 
        if int(mySpot) > float(x): 
            return 'No'
        else:
            x = mySpot
    return 'Yes'    
    

if __name__ == '__main__':
    for i in range(int(input())):
        numBlocks = int(input())
        blocks = deque(input().split())
        print(stack(numBlocks, blocks))
    


if __name__ == '__main__':
    #lstA = [4,3,2,1,3,4]
    #numBlocks = len(lstA)
    #blocks = deque(lstA)

    lstB = [1,3,2]
    numBlocks = len(lstB)
    blocks = deque(lstB)
    print(stack(numBlocks, blocks))
