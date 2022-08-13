
pos=-1

def search(input0,input1):
    i=0
    while i < len(input1):
       
        if input1[i]==input0:
            globals()['pos']=i
            return True,pos
        i=i+1
    else:
            return False

input0=int(input("enter"))
input1=list(map(int,input().split()))
if search(input0,input1):
    print("Found at",pos)
else:
    print("Not Found")