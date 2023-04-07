from tkinter import *
import tkinter .messagebox
import sqlite3 as sq
win1=Tk()
conn=sq.connect('Bookstore.db')
cursor=conn.cursor()
def book ():
    a=userid_entry.get()
    b=password_entry.get()
    userlist=['abhishek','kapil','roshan','aditi','jonathan','dhruv','deepak','anuj','anjney','naman']
    if a in userlist and b=='1234':
#<><><><><><><><><><><><><><>Book Store<><><><><><><><><><><><><><>       
        win=Toplevel()
        win.title('BOOK STORE')
#<><><><><><><><><><><><><><>Functions<><><><><><><><><><><><><><>
        def view():
            cursor.execute("SELECT * FROM Books;")
            a=cursor.fetchall()
            listbox.delete(0, END)
            for i in a:
                 listbox.insert(END,'Book:',i) 
        def add():
            id=id_entry.get()
            name=name_entry.get()
            author=author_entry.get()
            price=price_entry.get()
            cursor.execute("""INSERT INTO Books VALUES (?,?,?,?)""",(id,name,author,price) )
            listbox.delete(0, END)
            conn.commit()
        def update():
            global selected_tuple
            index=listbox.curselection()
            selected_tuple=listbox.get(index)
            update1(name_entry.get(),author_entry.get(),price_entry.get())
        def update1(name="",author="",price=""):
            cursor=conn.cursor()
            cursor.execute("UPDATE Books SET book_name=?,book_author=?,book_price=? WHERE book_id=? ",(name,author,price,selected_tuple[0]))
            listbox.delete(0, END)
            conn.commit()
        def search1():
            search(id_entry.get(),name_entry.get(),author_entry.get(),price_entry.get())
        def search(id="",name="",author="",price=""):
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Books WHERE book_id=? OR book_name=? OR book_author=? OR book_price=?",(id,name,author,price))
            a=cursor.fetchall()
            listbox.delete(0, END) 
            for i in a:
                listbox.insert(END,'Book:',i)
                conn.commit()  
        def delete():
           index=listbox.curselection()
           selected_tuple=listbox.get(index)
           cursor=conn.cursor()
           cursor.execute("DELETE FROM Books WHERE book_id=?;",(selected_tuple[0],))
           listbox.delete(0, END)
           conn.commit() 
        def close():
            tkinter.messagebox.showinfo('message','Thank You')
            win.destroy()
            win1.destroy()
        win.title('BOOK STORE')
#<><><><><><><><><><><><><><>Labels and Boxes<><><><><><><><><><><><><><>        
        scroll = Scrollbar(win,orient=VERTICAL)  
        scroll.grid(row=3,column=4,rowspan=6)
        space1=Label(win,text='  ',font=('',10))
        space1.grid(row=0,column=0,sticky=W)
        id=Label(win,text=' BOOK ID  ',font=('',15),fg='red')
        id.grid(row=0,column=1,sticky=W+E+S+N)
        id_entry=Entry(win,font=('',15))
        id_entry.grid(row=0,column=2)
        name=Label(win,text='  BOOK NAME',font=('',15),fg='red')
        name.grid(row=0,column=3,sticky=W+E+S+N)
        name_entry=Entry(win,font=('',15))
        name_entry.grid(row=0,column=5)
        space2=Label(win,text='  ',font=('',15))
        space2.grid(row=0,column=6,sticky=W+E+S+N)
        author=Label(win,text=' AUTHOR  ',font=('',15),fg='red')
        author.grid(row=1,column=1,sticky=W+E+S+N)
        author_entry=Entry(win,font=('',15))
        author_entry.grid(row=1,column=2)
        price=Label(win,text='  PRICE',font=('',15),fg='red')
        price.grid(row=1,column=3,sticky=W+E+S+N)
        price_entry=Entry(win,font=('',15))
        price_entry.grid(row=1,column=5)
        listbox=Listbox(win,width=40,yscrollcommand=scroll.set)
        listbox.grid(row=3,column=1,columnspan=3,rowspan=6)
        textfont=('times',15)
        listbox.config(font=textfont)
#<><><><><><><><><><><><><><>Buttons<><><><><><><><><><><><><><>        
        view_button=Button(win,text='VIEW ALL',fg='red',bg='black',command=view)
        view_button.grid(row=3,column=5,sticky=E+W+S+N)
        search_button=Button(win,text='SEARCH ENTRY',fg='red',bg='black',command=search1)
        search_button.grid(row=4,column=5,sticky=E+W+S+N)
        add_button=Button(win,text='ADD ENTRY',fg='red',bg='black',command=add)
        add_button.grid(row=5,column=5,sticky=E+W+S+N)
        update_button=Button(win,text='UPDATE SELECTED',fg='red',bg='black',command=update)
        update_button.grid(row=6,column=5,sticky=E+W+S+N)
        delete_button=Button(win,text='DELETE SELECTED',fg='red',bg='black',command=delete)
        delete_button.grid(row=7,column=5,sticky=E+W+S+N)
        close_button=Button(win,text='CLOSE',fg='red',bg='black',command=close)
        close_button.grid(row=8,column=5,sticky=E+W+S+N)
        space4=Label(win,text='  ',font=('',10))
        space4.grid(row=9,column=1,sticky=W)
        scroll.config(command=listbox.yview)
        win.geometry('730x300+120+120')
        scroll.config(command=listbox.yview)
    else:
        tkinter.messagebox.showinfo('message','Wrong UserId or Password')
#<><><><><><><><><><><><><><>LOG In Page<><><><><><><><><><><><><><>   
win1.title('BOOK STORE LOGIN')
#<><><><><><><><><><><><><><>Functions<><><><><><><><><><><><><><>   
def help():
    tkinter.messagebox.showinfo('help','Enter Your Name')
def help2():
    tkinter.messagebox.showinfo('help','Enter password')
def reset():
    userid_entry.delete('0',END)
    password_entry.delete('0',END) 
#<><><><><><><><><><><><><><>Labels and Boxes<><><><><><><><><><><><><><>       
space1=Label(win1,text='   ',font=('',10))
space1.grid(row=1,column=0,sticky=W)
space2=Label(win1,text='   ',font=('',10))
space2.grid(row=3,column=0,sticky=W)
space3=Label(win1,text='   ',font=('',10))
space3.grid(row=5,column=0,sticky=W)
space4=Label(win1,text='   ',font=('',10))
space4.grid(row=0,column=5,sticky=W)
l1=Label(win1,text='  LogIn Page  ',font=('',20),fg='red')
l1.grid(row=0,column=2,sticky=W)
userid=Label(win1,text='  UserId  ',font=('',15),fg='red')
userid.grid(row=2,column=1,sticky=W)
userid_entry=Entry(win1,font=('',15))
userid_entry.grid(row=2,column=2)
help=Button(win1,text='help',fg='red',bg='black',command=help)
help.grid(row=2,column=3)
password=Label(win1,text=' Password  ',font=('',15),fg='red')
password.grid(row=4,column=1,sticky=W)
password_entry=Entry(win1,font=('',15))
password_entry.grid(row=4,column=2)
#<><><><><><><><><><><><><><>Buttons<><><><><><><><><><><><><><>   
help2=Button(win1,text='help',fg='red',bg='black',command=help2)
help2.grid(row=4,column=3)
login_button=Button(win1,text='  \tLogin\t\t',fg='red',bg='white',command=book)
login_button.grid(row=6,column=1,sticky=E+W+S+N)
reset_button=Button(win1,text='\t\tReset\t\t',fg='red',bg='white',command=reset)
reset_button.grid(row=6,column=2,sticky=E+W+S+N)
win1.geometry('450x200+120+120')
win1.mainloop()

y=input()