terms=[]
for a in range(2, 101):
    for b in range(2, 101):
        if(a**b not in terms):
            terms.append(a**b)
print(len(terms))