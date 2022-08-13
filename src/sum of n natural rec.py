def calc(n):
    if n<0:
        return 0
    else:
        return n + calc(n-1)
n1=int(input())
print(calc(n1))