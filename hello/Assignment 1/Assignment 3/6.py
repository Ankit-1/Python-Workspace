def fact(a):
    i=a
    fact=1
    while(i>0):
       fact=fact*i
       i=i-1
    return fact
print("Enter the number:")   
a=int(input())
b=fact(a)       
print("factorial of {} is ".format(a),b)

    
