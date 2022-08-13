def check(n):
    l=len(n)
    for i in range(l):
        for j in range(i+1,l):
            if n[i]>n[j]:
                n[i],n[j]=n[j],n[i]
    print(n)
n1=list(map(int,input().split(" ")))
check(n1)