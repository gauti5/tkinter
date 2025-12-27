import tkinter as tk 
from tkinter import ttk 

window=tk.Tk()
window.title("My Application")

my_frame=ttk.Frame()
my_frame.pack(side='left', fill='both', expand=True)

label1=tk.Label(my_frame, text='Hello World', bg='green')
label1.pack(side='left', fill='y')  # 'y' -> vertical, 'x' -> Horizontal

label2=tk.Label(text="How are You", bg='red')
label2.pack(side='left', fill='y')

label3=tk.Label(text="Have a Nice Day", bg='orange')
label3.pack(side='right', fill='both', expand=True)

button=tk.Button(text="Click")
button.pack(side='bottom', fill='y', expand=True)

window.minsize(width=800, height=500)
window.mainloop()