sum=0
for i in range(5):
    print('enter the marks of',i+1,'subject::' )
    a=int(input(""))
    sum=sum+a
    avg=sum/5
print(avg)
if(avg>90):
    print("A+")
elif(avg>80 and avg<=90):
    print("A")
elif(avg>=70 and avg<=80):
    print("B")       
else:
    print("C")    
    