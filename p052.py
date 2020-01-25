def is_permutation(n1, n2):
    n1=str(n1)
    n2=str(n2)
    if(len(n1)!=len(n2)):
        return False
    for c in n1:
        if c not in n2:
            return False
    return True

def is_permutations(n1, list1):
    for item in list1:
        if not is_permutation(n1, item):
            return False
    return True
x=0
while(True):
    x+=1
    if(is_permutations(x, [2*x, 3*x, 4*x, 5*x, 6*x])):
        print(x)
        break