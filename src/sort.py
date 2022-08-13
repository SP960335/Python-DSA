class bubbles:
    def bsort(self,arr):
        #n=int(input())
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
            print(arr)
        return arr,arr[i]
obj=bubbles()
arr=list(map(int,input().split(" ")))
print(obj.bsort(arr))

