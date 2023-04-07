# from tkinter import *
#   
# win=Tk()               #BODY STARTS
# def func():
#     f=var2.get()
# #     print(f)
# #     print('Thanks for logging in...')
#     c.delete('1.0',END)        #deletes the previous input  #1.0 has to be put,predefined
#     c.insert(END,f)            #END puts the input at end 
# win.title('JIMS') 
# a=Button(win,text='LOGIN',command=func)
# # a.pack(side='bottom')   
# a.grid(row=0,column=0)
# var2=StringVar()
# b=Entry(win,text=var2,font=('',20))   #text=var2  used to display input entered in entry in Text
# b.grid(row=0,column=1)
# c=Text(win,height=20,width=15)
# c.grid(row=1,column=0)
# var=StringVar()
# d=OptionMenu(win,var,'BCA','BJMC','BBA')
# d.grid(row=0,column=3)
# l1=Label(win,text='JIMS',bg='blue',fg='#fff',font=('',20))
# l1.grid(row=2,column=1,sticky=S)
#   
# win.mainloop()    #BODY CLOSE



from tkinter import *
     
win=Tk()               #BODY STARTS
def func():
    f=eval(v.get())
    g=(f)*1000
    t=f*2.20462
    t1=f*35.274
    c.insert(END,g)
    d.insert(END,t)
    e.insert(END,t1)
win.title('tk')
l1=Label(win,text='Kg')
l1.grid(row=0,column=0,sticky=E)
v=StringVar()
b=Entry(win,text=v)
b.grid(row=0,column=1)
a=Button(win,text='CONVERT',command=func)
a.grid(row=0,column=2)
c=Text(win,height=1,width=20)
c.grid(row=1,column=0)
d=Text(win,height=1,width=20)
d.grid(row=1,column=1)
e=Text(win,height=1,width=20)
e.grid(row=1,column=2)
    
win.mainloop()


# from tkinter import *
#  
# class BuckysButtons:
#      
#     def __init__(self,master):
#         frame=Frame(master)
#         frame.pack()
#      
#         self.printButton=Button(frame,text="Print Message",command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#      
#         self.quitButton=Button(frame,text="Quit",command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#      
#     def printMessage(self):
#         print("Wow, this actually works ")
#          
# root=Tk()
# b=BuckysButtons(root)
# root.mainloop()