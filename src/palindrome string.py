def comp(s1):
    s2=s1[::-1]
    if s1==s2:
        print("plaindrome")
    else:
        print("not a palindrome")
s=input()
comp(s)