def swappu(s):
    s=s.replace(", ","third")
    s=s.replace(".",", ")
    s=s.replace("third",".")
    return s
s2=input()
print(swappu(s2))