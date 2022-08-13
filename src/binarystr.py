def check(string):
    s=set(string)
    l={'0','1'}
    if s==l or s=='0' or s=='1':
        print("binary string")
    else:
        print("not binary")
inp=input()
check(inp)