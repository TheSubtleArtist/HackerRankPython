"""
Let's dive into decorators! 
You are given N mobile numbers. 
Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual digit number. 
Alternatively, there may not be any prefix at all.

Input Format:
The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.

Output Format:
Print N mobile numbers on separate lines in the required format.

Concept

Like most other programming languages, Python has the concept of closures. 
Extending these closures gives us decorators, which are an invaluable asset. 
You can learn about decorators in 12 easy steps here.
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. 
Make a decorator that standardizes the mobile numbers and apply it to the function.

Sample Input:
3
07895462130
919875641230
9195969878

Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""

"""
Long Form Solution:


number = list()

N = int(input())

for i in range (N):
    number.append(str(input()))

def wrapper(f):
    def fun(l):
        return sorted([function(i) for i in number])
    return (fun)

@wrapper
def standardize(number):
    return ("+91" + " ") + number[-10:-5] + " " + number[-5:]

print('\n'.join(standardize(number)))
"""


# Solution:

def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
