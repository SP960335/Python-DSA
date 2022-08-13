def uncom(a,b):
    x=a.split()
    y=b.split()
    d={}

    for i in x:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in y:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)

    for i in d:
        if(d[i]==1):
            print(i)

p=input()
q=input()
uncom(p,q)

def uncom(a,b):
    a=a.split()
    b=b.split()
    k=set(a).symmetric_difference(set(b))
    return k
   
p=input()
q=input()
print(list(uncom(p,q)))



            
