import addmath
counter=0
for n in range(1, 101):
    for r in range(1, n):
        if(addmath.combinations(n, r)>1000000):
            counter+=1
print(counter)