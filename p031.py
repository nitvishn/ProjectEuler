coins=[1, 2, 5, 10, 20, 50, 100, 200]

def ways(target, avc):
    if(avc<=1):
        return 1
    res=0
    while target>=0:
        res+=ways (target,avc -1)
        target-=coins[avc-1]
    return res

amount=200
print (ways(amount , 8))