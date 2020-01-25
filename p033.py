import itertools

def digitCommonButNotZero(num1, num2):
	num1=str(num1)
	num2=str(num2)
	if '0' in num1 or '0' in num2:
		return False
	for char in num1:
		if char in num2 and char!='0':
			return char
	return False

def testProperty(num, denom):
	char = digitCommonButNotZero(num, denom)
	if not char:
		return False
	if num>=denom:
		return False
	num2=int(str(num).replace(char, '', 1))
	denom2=int(str(denom).replace(char, '', 1))
	if num/denom == num2/denom2:
		return True
	return False

fractions=[]
for num in range(10, 100):
	for denom in range(10, 100):
		if testProperty(num, denom):
			fractions.append((num, denom))

print(fractions)