strr=str(input())
n=(len(strr))//2
print(n)
for i in range(len(strr)):
    if i>=n:
        res=strr[i].upper()
        print(",".join(map(str,strr[i])))