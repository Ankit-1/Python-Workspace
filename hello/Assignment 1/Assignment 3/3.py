def calc(a,b):
    print("1.sum \
           2.division \
           3.multiplication\
           4.substraction")
    print("enter the choise")
    a=int(input())
    if(a==1):
        c="sum"
        return a+b,c
    elif(a==2):
        c="division"
        return a/b,c
    elif(a==3):
        c="multiplication"
        return a*b,c
    else:
        c="sub"
        return a-b,c0
    
b=calc(7,4)
print("the {} is {}".format(b[1],b[0]))    
    