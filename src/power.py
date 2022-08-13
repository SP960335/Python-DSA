def pwr(n,p):
    if(p==0):
        return 1
    elif(p==1):
        return n
    else:
        return(n*pwr(n,p-1))
n=int(input())
m=int(input())
print(n,'^',m,'=',pwr(n,m))