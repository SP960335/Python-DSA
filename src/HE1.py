# class count:
#     def freq(self,arr):
#         count=0
#         n=len(arr)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if arr[i]==arr[j]:
#                     count=count+1
#         return count
# obj=count()
# print(obj.freq(list(map(int,input().split()))))

t=int(input())
while t:
        t=t-1
        arr=list(map(int,input().split(" ")))
        n,k=arr[0],arr[1]
        arr1=list(map(str,input().split(" ")))
        #print(t,n,k,arr,arr1)
        result=[]
        1,2,3,4,5
        k=k%n
        for i in range(n-k,n):
            result.append(arr1[i])
        for i in range(0,n-k):
            result.append(arr1[i])
        print(" ".join(result))

            
