"""
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Input Format

The first line contains the first name, and the second line contains the last name.


"""


def print_full_name(first, last):
	print(f'Hello {first} {last}! You just delved into python.')
	return


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
