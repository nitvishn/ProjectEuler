digits=['1', '2', '3', '4', '5', '6', '7', '8', '9']

def not_repeating(number):
    nums=[]
    for num in str(number):
        if num in nums or num=='0':
            return False
        nums.append(num)
    return True

def get_other_digits(number):
    number = str(number)
    digits_copy = digits[:]
    for element in number:
        del digits_copy[digits_copy.index(element)]
    return digits_copy

nums=[]
for i in range(1, 10000):
    if(not_repeating(i)):
        nums.append(i)
products=[]
for n in nums:
    for m in nums:
        number=str(n*m)+str(n)+str(m)
        if(not_repeating(number) and len(number)==9 and n*m not in products):
            print(n*m, n, m)
            products.append(n*m)
print(sum(products))