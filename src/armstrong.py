# #def arms(n):
# n=int(input())
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if n==sum:
#       print("Armstrong")
# else:
#         print("not armstrong")

def arms(lower,upper):
    
    for n in range(lower,upper+1):
        sum=0
        order=len(str(n))
        temp=n
        while temp>0:
            digit=temp%10
            sum=sum+digit**order
            temp=temp//10
        if n==sum:
            print("armstrong",n)
        
p=int(input())
k=int(input())
arms(p,k)


