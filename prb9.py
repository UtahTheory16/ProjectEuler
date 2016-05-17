import numbers
from math import sqrt
total = 0
product = 0
for a in range(1,1001):
	for b in range(1,1001):
		d = a**2+b**2
		c = sqrt(d)
		total = a+b+c
		#print total
		if total == 1000:
			product = a*b*c
			print product
			break
