def details(name,age=14,surname='Mehta'):       #all the arguments after default argument should be default.
    name=name+' '+surname
    return age+6,name


# a,b=details('Anuj', 14, 'Mehta')
# # print("NAME is ",a[1],'AGE is',a[0]) // unpacking a tuple through indexing
# print("NAME is",b,'AGE is',a)

# a,b=details(name='Anuj',surname='Mehta',age=14) #using positional arguments
# print("NAME is",b,'AGE is',a)

a=details('Taarak') #default argument use
print('Your name is',a[1],'Your age is',a[0])
