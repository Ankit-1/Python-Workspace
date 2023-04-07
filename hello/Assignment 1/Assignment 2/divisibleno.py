print("enter the range in which you want to find the number......")
a=int(input())
b=int(input())
print("enter the number for division")
c=int(input())
for i in range(a,b):
    if(i%c==0):
        print(i)
    