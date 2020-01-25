import sys

def ispalindrome(n):
    if int(str(n)[::-1])==n:
        return True
    return False

digits=3
current=0
for i in range((10**(digits-1)),10**digits):
    for n in range((10**(digits-1)),10**digits):
        if ispalindrome(i*n) and i*n>current:
            current=i*n
print(current)