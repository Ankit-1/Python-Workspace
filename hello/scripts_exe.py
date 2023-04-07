
def area():
    print('Shapes: 1.triangle\
    2. rectangle\
    3.Square\
    4.Circle')
    print('Enter your choice from 1-4') 
    a=input()
    a=int(a)
    if(a==1):
        print('Enter the base of your triangle')
        b=input()
        b= int(b)
        print('Enter the height of your triangle')
        c=input()
        c= int(c)
        ans= 0.5*b*c
        print('output of "triangle" from "area" function is:-',ans)
    elif(a==2):
         print('Enter the length of your rectangle')
         b=input()
         b= int(b)
         print('Enter the breadth of your rectangle')
         c=input()
         c= int(c)
         ans= b*c
         print('output of "rectangle" from "area" function is:-',ans)
          
    elif(a==3):
         print('Enter the side of your square')
         b=input()
         b= int(b)
         ans=4*b
         print('output of "square" from "area" function is:-',ans)
    elif(a==4):
         print('Enter the radius of your circle')
         b=input()
         b= int(b)
         ans=3.14*b*b
         print('output of "square" from "area" function is:-',ans)
    else:
        print('not valid')
     
 
g=area()  

def check(d):
    if(d%2==0):
     type='Even'
    else:
     type='odd'
     
    return type,d
# print('Enter the number to check')
# a=input()
# a=int(a)
#  
#  
#      