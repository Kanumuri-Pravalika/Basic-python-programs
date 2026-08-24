s=input("Enter any sentence : ")
d={}
words=s.split()
for word in words:
    word=word.lower()
    if word in d:
         d[word]+=1
    else:
        d[word]=1
print(d)
       