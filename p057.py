import addmath

numer=2
denom=3
count=0

for i in range(1000):
    numer+=2*denom
    denom=numer-denom
    print(numer, denom)
    if(len(str(numer))>len(str(denom))):
        count+=1
print(count)