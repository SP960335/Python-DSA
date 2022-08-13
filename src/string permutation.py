def permut(s,start):
    if(start==len(s)):
        print("".join(s))
        return
    for i in range(start,len(s)):
        s[start],s[i]=s[i],s[start]
        permut(s,start+1)
        s[start],s[i]=s[i],s[start]
    return

str=input()
permut(list(str),0)