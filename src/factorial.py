def facto(n):
   # return 1 if (n==1 or n==0) else n * facto(n - 1);
    factorial=1
    k=5
    for i in range(1,k+1):
     while n>1:
        factorial=factorial*n
        n=n-1
     return factorial

n1=int(input())
print(facto(n1))

