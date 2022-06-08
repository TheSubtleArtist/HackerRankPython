"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N x M. (N is an odd natural number, and M is 3 times N
.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""


n=9
m=27
message = 'WELCOME'
pattern = '.|.'
#n, m = map(int,input().split())

#Prints Top Pattern
for i in range(1, n, 2):
	print((pattern * i).center(m,'-'))



#Prints Welcome Line
print(message.center(m,'-'))


#Prints Bottom Pattern
for i in range(n-2, -1, -2):
	print((pattern * i).center(m,'-'))