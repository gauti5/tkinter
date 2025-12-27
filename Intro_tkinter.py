# Tkinter --> Tkinter is builtin python library for creating a graphical user interface. It help us to create a GUI application.

import tkinter
import tkinter.font as tfont

# Tk Module --> helps us to create a window

window=tkinter.Tk()
window.title("My Application") # Title of the Application

# Default size
window.minsize(width=800, height=600)

# Custom Font
# Custom_font=tfont.Font(family='Times New Roman', size=50, slant='italic', weight='bold')

# Add a text inside a window that we can create with help of class (Label)
# label=tkinter.Label(text="Welcome to My Application!!", font=("Times New Roman", 50, 'bold'))
# label=tkinter.Label(text="Welcome to My Application!!", font=custom_font)
label=tkinter.Label(text="Welcome to My Application!!")  # it wont show anything in the window if we are not using pack() method


# by Default it shows the text in the Center we can change the postion 
# label.pack(side='left')  
# label.pack(expand=1) # center alignment

label.pack()  # brings the text in the window & and also automatically resize the window size based on the text size if we are not using the minsize() method.


# changing the font settings
label.config(font=("Courier New", 50, "underline", 'bold'))

# Changing the text
# one way -> label['text']
# label['text']="Welcome"
# Another way -> using config
label.config(text="My New Application")

'''
counter=0
def funtion_button():
    # print("Thanks for clicking the button!!")
    global counter
    counter=counter+1
    label.config(text=f"The button got clicked {counter} times")
'''

def funtion_button():
    user_input_text=user_input.get()
    label.config(text=user_input_text)

# Taking user input using entry
user_input=tkinter.Entry(width=20, show="*") # show -> masking the content
user_input.pack()

# Buttons -> clickable component in the windows
button=tkinter.Button(text="Click", font=('Times new Roman', 40, 'bold'), command=funtion_button)
button.pack()


# mainloop --> help us to see the window and keeps it open until we close it manually.
window.mainloop()