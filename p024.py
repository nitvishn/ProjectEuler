from itertools import permutations
string='0123456789'
perms=[]
count=0
for perm in permutations(string, len(string)):
    count+=1
    if(count==1000000):
        print(perm)
        break
perms.sort()
print(perms)