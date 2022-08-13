TODO:0#Reverse without extended slice and only the words not entire sequence
# x=list(map(str,input().split()))
# y=[]
# for word in  range(len(x)-1,-1,-1):
#     for i in word:
#         y.append(i)
# print(y)





# TODO:1
str='starlight in the moon'
str1=''
for i in range(len(str)-1,-1,-1):
    str1=str1+str[i]
print(str1)


# TODO:2
# class rev:
#     def strrev(self,str3):
#         str3=str3[-1::-1]
#         strr=" ".join(str3)
#         return strr
# obj=rev()
# str1=str(input("Enter string:"))
# str2=str1.split(" ")
# print(str1)
# print(obj.strrev(str2))


# TODO:3
# def reverse(string):
#     string=string[::-1]
#     return string
# s='shatakshi'
# print(reverse(s))
# print(s)