a = 100
b = 1000
palindromes = []
def rev(number):
	return number == int(str(number)[::-1])

for i in xrange(a,b):
	for j in xrange(a,b):
		num = i*j
		if rev(num):
			palindromes.append(num)

sorted(palindromes)
print max(palindromes)




