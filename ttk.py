from tkinter import ttk # better version of tkinter
import tkinter

window=tkinter.Tk()
window.title("New Application")
window.minsize(width=800, height=500)

label=ttk.Label(text="Welcome to the Application!!", font=('Calibri', 50, 'bold'))
label.pack()


def funtion_button():
    user_input_text=user_input.get()
    label.config(text=user_input_text)

# Taking user input using entry
user_input=ttk.Entry(width=20, show="*") # show -> masking
user_input.pack()

# Buttons -> clickable component in the windows
button=ttk.Button(text="Click", command=funtion_button)
button.pack()

# Button -> To destroy the window
quit_button=ttk.Button(text="Quit", command=window.destroy)
quit_button.pack() 

window.mainloop() 