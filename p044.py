def pentagonalGen():
    diff=4
    num=1
    while(True):
        yield num+diff
        num+=diff
        diff+=3

n=1
for number in pentagonalGen():
    if(number>5482660):
        break
    elif(number==5482660):
        print(n)
        break
    n+=1

c=5482660
k = c+1
i = k+1
while i <= c**2:
    while i<k:
        i = i + 1
    print(c, k, i)
    if 3*(c**2 + 2*k**2 - i**2)+2*k-i+c==0:
        print(c,k,i)
        break
    k = k + 1
    break