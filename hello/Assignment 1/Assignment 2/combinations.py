print("enter the three numbers")
a=int(input())
b=int(input())
c=int(input())
li=[]
li.append(a)
li.append(b)
li.append(c)
print(li)
for i in li:
    for j in li:
        for k in li:
            print(i,j,k)
