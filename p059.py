import itertools
words=[]
dict_file=open("large", 'r')
for word in dict_file:
    words.append(word.replace('\n', ''))

def checkString(words, string):
    count=0
    for word in words:
        if(word in string):
            count+=1
    return count

def xor(data, key):
    return ''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(data, itertools.cycle(key)))

def getKeys():
    chars=[]
    for i in range(97, 97+26):
        chars.append(chr(i))
    keys=[]
    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                keys.append(char1+char2+char3)
    return keys

def getData(filename):
    file=open(filename, "r")
    ciphercode=""
    for line in file:
        arr=line.split(",")
        for item in arr:
            ciphercode+=chr(int(item))
    return ciphercode

def applyKey(key, data):
    plaintext=xor(data, key)
    return plaintext

# #GET OUTPUT
# file='p059_cipher.txt'
# keyfile=open('p059_keyfile.txt', 'r')
# data=getData(file)
# best_string=None
# best_count=0
# keys=getKeys()
# badkeys=[]
# for line in keyfile:
#     line=line.replace('\n', '')
#     badkeys.append(line)
# keys = list(set(keys) - set(badkeys))
# keyfile=open('p059_keyfile.txt', 'a')
# print(keys)
# for key in keys:
#     dec_data=applyKey(key, data)
#     curr_count=checkString(words, dec_data)
#     if(curr_count>best_count):
#         best_count=curr_count
#         best_string=dec_data
#     else:
#         keyfile.write(key + '\n')
#     print(best_string)

outfile=open("p059_outfile.txt", "r")
string=""
for line in outfile:
    string+=line
string.replace("\n", "")
vals=[]
for char in string:
    vals.append(ord(char))
print(string)
print(sum(vals))
