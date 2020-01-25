import addmath

def binary(number):
    return int(bin(number)[2:])

def palindrome(number):
    number=str(number)
    if(len(number)<=1):
        return True
    if(number[0]==number[-1]):
        return palindrome(number[1:-1])
    return False

palindromes=[]
for i in range(1, 1000000):
    if(palindrome(i) and palindrome(binary(i))):
        palindromes.append(i)
print(sum(palindromes))