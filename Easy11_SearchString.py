"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

The first line of input contains the original string. The next line contains the substring.
"""

def count_substring(string, sub_string):
	count = 0
	for i in range(len(string)):
		if string[i:].startswith(sub_string):
			count += 1
	return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


"""
#Complex Solution
string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))

"""