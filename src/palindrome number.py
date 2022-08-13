def palindrome(n):
   
   temp=n
   temp=temp[::-1]
   
   if n==(temp):
       print("palindrome")
    

n=input()
palindrome(n)