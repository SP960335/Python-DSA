def comp(l2):
    l2=l2.split()
    ct=0
    for i in range(0,int(input())):
        if l2[i]<l2[i+1] and l2[i]<l2[i-1]:
            ct+=1
    print(ct)
