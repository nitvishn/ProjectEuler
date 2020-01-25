import addmath
def pandigital(number):
    number_set = addmath.get_digits(number)
    if(len(number_set)!=len(str(number)) or 0 in number_set):
        return False
    for i in range(1, 10):
        if i not in number_set:
            return False
    return True

def genProducts():
    num=1
    while(True):
        prodsum=''
        digits=range(1,num)
        for element in digits:
            prodsum+=str(element*num)
            if(pandigital(prodsum)):
                yield prodsum
            if(len(prodsum)>10):
                break
        num+=1

for i in genProducts():
    print(i)