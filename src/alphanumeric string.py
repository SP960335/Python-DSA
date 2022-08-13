def alphanum(n):
    flag1=False
    flag2=False

    for i in n:
        if i.isalpha():
            flag1=True
        if i.isdigit():
            flag2=True
    return flag1 and flag2
n=input()
print(alphanum(n))