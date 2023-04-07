from tkinter import *
class MyButtons:
    def __init__(self,master):
        frame = Frame(master).pack()
                
        self.printButton = Button(frame,text='Print Message',command=self.printMessage()).pack(side=LEFT)
        self.quitButton = Button(frame,text='QUIT',command=quit).pack()
        
        
    def printMessage(self):
        print("This atually worked!!")
        
root = Tk()
b = MyButtons(root)
root.mainloop()