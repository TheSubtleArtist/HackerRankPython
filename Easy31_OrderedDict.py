"""
collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.


"""

from collections import OrderedDict

products = OrderedDict()
foodList = OrderedDict()
N = int(input())



for i in range(N):
	item, space, price = input().rpartition(' ')
	if item in foodList:
		foodList[item] += int(price)
	else:
		foodList[item] = int(price)

for key, value in foodList.items():
	print(key, value)

