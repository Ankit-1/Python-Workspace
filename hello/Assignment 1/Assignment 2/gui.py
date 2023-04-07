from tkinter import *
 
win=Tk()
def func():
    f=eval(v.get())
    f1=var.get()
    f2=v2.get()
    if(f2=="kg"):
       if(f1=="g"):
           g=f*1000
       elif(f1=="pounds"):
           g=f*2.20426
       elif(f1=="ounces"):
           g=f*35.274        
    l2.config(text=str(g))
def fun():
    win.quit()
win.title('tk')
v2=StringVar()
l1=OptionMenu(win,v2,"kg","pounds","ounces")
l1.grid(row=0,column=0,sticky=E)
v=StringVar()
b=Entry(win,text=v)
b.grid(row=0,column=1)
var=StringVar()
d1=OptionMenu(win,var,"g","pounds","ounces")
d1.grid(row=0,column=3)
l2=Label(win,text="...")
l2.grid(row=0,column=2,sticky=E)
a=Button(win,text='Convert',command=func)
a.grid(row=1,column=1)
a=Button(win,text='close',command=fun)
a.grid(row=1,column=2)

 
win.mainloop()
