def triangleGen():
    number=0
    prev=-1
    while(True):
        number+=prev+1
        prev+=1
        yield number

def getValue(word):
    word = word.upper()
    sumall=0
    for letter in word:
        sumall+=ord(letter)-64
    return sumall
    
file = open("p042_words.txt", 'r')
for line in file:
    pass
line=line.split(',')
words=[]
triangles=set()
for num in triangleGen():
    if(num>200):
        break
    triangles.add(num)
for word in line:
    words.append(word.replace('"', ''))
num=0
for word in words:
    val=getValue(word)
    if(val in triangles):
        # print(word, end=' ')
        num+=1
print(num)