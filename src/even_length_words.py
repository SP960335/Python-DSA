str1=str(input())
str2=str1.split()
print(str2)
for word in str2:
     if len(word)%2==0:
         print(word,len(word))


