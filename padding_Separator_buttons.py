
import tkinter
import tkinter.font as tfont
from tkinter import ttk 


window=tkinter.Tk()
window.title("My Application") # Title of the Application

# Default size
window.minsize(width=800, height=600)

label=ttk.Label(text="Welcome to My Application!!", padding=20)  # it wont show anything in the window if we are not using pack() method


label.pack()  


def funtion_button():
    user_input_text=user_input.get()
    label.config(text=user_input_text)

# Taking user input using entry
user_input=tkinter.Entry(width=20, show="*") # show -> masking the content
user_input.pack()

# Buttons -> clickable component in the windows
button=tkinter.Button(text="Click", font=('Times new Roman', 20, 'bold'), command=funtion_button)
button.pack()

# create the text box for multilines

text=tkinter.Text(height=15, width=25) # At a time shows 10 lines, remaining will be hidden in the screen.
text.pack()
text.focus() # cursor will be blink

text.insert("1.0", "Enter your Comments") # Default text
# 1->first line, 0->1st character

text['state']='disabled' # text cant be removed

def enable_text():
    text['state']='normal'
    
enable_button=tkinter.Button(text="Enable Text", font=('Times new roman', 20, 'bold'), command=enable_text)

enable_button.pack(pady=15) # pady -> padding y axis

# text_data=text.get("1.0", 'end')
# print(text_data)

# padding -> to keep some distance b/w the components


# Separator
sep=ttk.Separator(orient='horizontal')
sep.pack(fill='x', pady=15)

# get the text in console
def text_function():
    text_data=text.get("1.0", 'end')
    print(text_data)
    
text_button=tkinter.Button(text='get text', command=text_function)
text_button.pack()

# check button
check_option=tkinter.BooleanVar()
# 1 -> check, 0 -> uncheck

def check_option_task():
    print(check_option.get(), type(check_option.get()))
    
check_button=ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, command=check_option_task, onvalue="True", offvalue="False")
check_button.pack()

# radio Button

radio_value=tkinter.StringVar()

def get_radio_value():
    print(radio_value.get())

radio_button1=ttk.Radiobutton(text='Male', variable=radio_value, value='male')
radio_button2=ttk.Radiobutton(text='Female', variable=radio_value, value='female')

radio_button1.pack()
radio_button2.pack()

# combo box
selected_country=tkinter.StringVar()
countries=ttk.Combobox(textvariable=selected_country, values=("India", "US", "Canada", "Australia", "England"))
countries['state']='readonly'
countries.pack()

def display_country(event):
    print(f"selected country is {selected_country.get()}")

# print in the console
countries.bind("<<ComboboxSelected>>", display_country)

# List Box
food_items=("Nachos", "Biryani", "Pizaa", "Noodles", "Salad")
selected_food=tkinter.StringVar(value=food_items)

# selectmode='extended' -> able to select mutliple from the list
food_list=tkinter.Listbox(listvariable=selected_food, height=5, selectmode='extended')
food_list.pack()

def get_fav_food(event):
    food_indices=food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))
        
food_list.bind('<<ListboxSelect>>', get_fav_food)

# Spin Box

def get_spin_box_value():
    print(f"Current spinbox value : {spin_box.get()}")
counter=tkinter.IntVar(value=10) # intial value will be shown as 10 in spinbox
spin_box=ttk.Spinbox(from_=0, to=20, textvariable=counter,wrap=True, command=get_spin_box_value)
spin_box.pack()

print(f"Initial Spinbox Value : {spin_box.get()}")
        
        

# mainloop --> help us to see the window and keeps it open until we close it manually.
window.mainloop()