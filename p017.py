numwords={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",1000:"onethousand"}
def word(number):
    temp=""
    while(not number==0):
        if number in numwords.keys():
            temp+=numwords[number]
            break
        if(number>100):
            temp+=numwords[int(str(number)[0])]
            number-=int(str(number)[0])*100
            temp+="hundred"
            if(not number==0):
                temp+="and"
            continue
        if(number>10):
            temp+=numwords[int(str(number)[0])*10]
            number-=int(str(number)[0])*10
            continue
    return temp

wordlen=0
for number in range(1001):
    wordlen+=len(word(number))
print(wordlen)