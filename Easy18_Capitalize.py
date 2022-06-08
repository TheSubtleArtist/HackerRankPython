"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
 For example, alison heck should be capitalised correctly as Alison Heck.

"""


def solves(s):
	ltrs = s.split()
	return ' '.join((word.capitalize() for word in ltrs))





s = 'one 1 t2o thr33 4our'

result = solves(s)
print(result)
