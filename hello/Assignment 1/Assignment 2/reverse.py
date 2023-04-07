print("enter the number you want to reverse")
a=int(input())
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print("the reverse of the no is:",rev)    