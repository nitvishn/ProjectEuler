import addmath

def isPalindrome(n):
    n=str(n)
    if(len(n)<1):
        return True
    if(n[0]!=n[-1]):
        return False
    return isPalindrome(n[1:-1])

numbers=set()
    
def lychrel(n):
    for i in range(50):
        n+=int(str(n)[::-1])
        if(isPalindrome(n)):
            return False
    return True

tot=0
for i in range(1, 10000):
    if(lychrel(i)):
        tot+=1
print(tot)