class MyClass: #creating a class
    a=10
    
p=MyClass() #creating an object of class
print(p.a)

class Person:
    def __init__(self,name,age): #built in function;exectuted when class is initiated 
        self.name= name          #Use the __init__() function to assign values to object properties, 
        self.age= age            #or other operations that are necessary to do when the object is being created
    def myfunction(self):
        print("Hello My Name is "+self.name)
        print('and my age is '+ str(self.age))
                
p1=Person('Austin',30)
p1.myfunction()

p2=Person('John',50)
p2.myfunction()

p2.name='Mitch' #to modify object properties

p2.myfunction()

del p2.age #to delete object property

p2.myfunction()

del p2 #delete object

p2.myfunction()