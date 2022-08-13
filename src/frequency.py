
# class freq:
#     def count(self,d):
#         d1={}
#         for i in d1:
#             d1[i]=d1.get(i,0) +1
#         print(d1)

# d2=str(input())
# d3=d2.split()
# obj=freq()
# print(obj.count(d3))
class freq:
    def count(self,n):
        k=n.split()
        d={}
        for i in k:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        return d
obj=freq()
n=str(input())
print(obj.count(n))