def freq(s):
    k=s.split()
    d={}
    for i in k:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        print(""+i+" "+str(d[i])+ " ")

inp1=input()
freq(inp1)