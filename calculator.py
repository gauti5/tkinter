# Step - 1 : Importing

from tkinter import *

# Step - 2 : GUI interaction

window=Tk()
window.geometry('500x500')

# Step - 3 : Adding inputs

# Entry Box
e=Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result=e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Buttons
b=Button(window, text='1', width=8, command=lambda:click(1))
b.place(x=10, y=60)

b=Button(window, text='2', width=8, command=lambda:click(2))
b.place(x=115, y=60)

b=Button(window, text='3', width=8, command=lambda:click(3))
b.place(x=220, y=60)

b=Button(window, text='4', width=8,  command=lambda:click(4))
b.place(x=10, y=100)

b=Button(window, text='5', width=8, command=lambda:click(5))
b.place(x=115, y=100)

b=Button(window, text='6', width=8, command=lambda:click(6))
b.place(x=220, y=100)

b=Button(window, text='7', width=8, command=lambda:click(7))
b.place(x=10, y=140)

b=Button(window, text='8', width=8, command=lambda:click(8))
b.place(x=115, y=140)

b=Button(window, text='9', width=8, command=lambda:click(9))
b.place(x=220, y=140)

# Operators 
def add():
    n1=e.get()
    global math 
    math='addition'
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='+', width=8, command=add)
b.place(x=10, y=180)

b=Button(window, text='0', width=8, command=lambda:click(9))
b.place(x=115, y=180)

def sub():
    n1=e.get()
    global math 
    math='subtraction',
    global i 
    i=int(n1)
    e.delete(0, END)
    
b=Button(window, text='-', width=8, command=sub)
b.place(x=220, y=180)

def mult():
    n1=e.get()
    global math
    math='multiplication'
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='*', width=8, command=mult)
b.place(x=10, y=220)

def div():
    n1=e.get()
    global math
    math='divison'
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text='/', width=8, command=div)
b.place(x=115, y=220)

def equal():
    n2=e.get()
    e.delete(0, END)
    if math=='addition':
        e.insert(0, i+int(n2))
    elif math=='subtraction':
        e.insert(0, i-int(n2))
    elif math=='multiplication':
        e.insert(0, i*int(n2))
    elif math=='divison':
        e.insert(0, i/int(n2))

b=Button(window, text='=', width=8, command=equal)
b.place(x=220, y=220)

def clear():
    e.delete(0, END)
    
b=Button(window, text='Clear', width=8, command=clear)
b.place(x=115, y=260)


# Step - 4 : mainloop

window.mainloop()