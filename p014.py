def seq(n):
    steps=1 #the number itself is the first step
    while(n>1):
        if(n%2==0):
            n/=2
        else:
            n=3*n+1
        steps+=1
    return steps
n=2
maxnum=n
maxseq=seq(n)
while(n<1000000):
    if(seq(n)>maxseq):
        maxnum=n
        maxseq=seq(n)
    n+=1
print(maxnum)