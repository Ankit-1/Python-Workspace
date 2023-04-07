print("enter the number you want to reverse")
a=int(input())
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10  
if(rev==a):
    print('no is palindrone')
else:
    print('it is not palindrone')    