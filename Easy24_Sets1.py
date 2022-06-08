"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Task:
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

"""

def average(array):
    # your code goes here
    x = list(dict.fromkeys(array)) #removes any duplicate values from the array
    y = len(x)
    z = sum (x)
    return z / y

array = [ 10 ,20, 30 , 40, 50, 60, 60 , 10 , 70 , 90]

print(average(array))