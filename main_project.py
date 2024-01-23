from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TES:S alchemy helper")
root.geometry("450x450")
start = True
main_menu = False

def click_start():
    global start, main_menu, label
    start= False
    main_menu = True
    label.config(text="Button is pressed")



if (start):
    label = Label(text="Hello, press one of the buttom down",font=("Arial",16))
    label.pack()
    button_start = ttk.Button(text="Start", command=click_start)
    button_start.pack(fill=X, padx=[40,40])
    button_setting = ttk.Button(text="Setting", command=click_start)
    button_setting.pack(fill=X, padx=[40,40])
    button_about = ttk.Button(text="About", command=click_start)
    button_about.pack(fill=X, padx=[40,40])
    button_exit = ttk.Button(text="K", command=click_start)
    button_exit.pack(fill=X, padx=[40,40])

if (main_menu):
    label = Label(text="Main menu")
    label.pack()



root.mainloop()