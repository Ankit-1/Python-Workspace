def global_local(x,y):
    global a 
    a=42 
    x,y = y,x
    b=33
    b=17
    c=100
    print(a,b,x,y)

a,b,x,y=1,15,3,4

global_local(17, 4)
print(a,b,x,y)