import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time


# defining the master gui box
master = tk.Tk()
master.geometry('300x300')
master.title('motor_menu_main')


# creating start button image
start_image = Image.open('/Users/portal2/Desktop/Hydrovia/python/START_button.png')
start_image = start_image.resize((25, 25), Image.ANTIALIAS)
start_image = ImageTk.PhotoImage(start_image)


# creating kill button image
kill_image = Image.open('/Users/portal2/Desktop/Hydrovia/python/KILL_button.png')
kill_image = kill_image.resize((25, 25), Image.ANTIALIAS)
kill_image = ImageTk.PhotoImage(kill_image)

# creating and placing the background
background_image = ImageTk.PhotoImage(Image.open('/Users/portal2/Desktop/Hydrovia/python/background.png'))
background = Frame(master, width=200, height=100)
background.pack()
background.place(anchor='center', relx=0.5, rely=0.5)

label_background = Label(background, image=background_image)
label_background.pack()

# "Main Motor Control"
label_title = tk.Label(master, text='Main Motor Control Menu')
label_title.place(relx=0.5, rely=0.2, anchor='center')


# Environmental control interface #
def button_envr_callback():
    if label_envr['text'] == 'Ready':
        label_envr['text'] = 'Running'
        messagebox.showinfo('System_Status:', 'Envr Control Now Running.')
    else:
        label_envr['text'] = 'Ready'


# label and button entities
label_envr = tk.Label(master, text='Ready')
button_envr = tk.Button(master, text='  Envr Ctrl  ', image=start_image, command=button_envr_callback, compound=tk.TOP)

# label and button positions & plotting
label_envr.place(relx=0.7, rely=0.4, anchor='center')
button_envr.place(relx=0.4, rely=0.4, anchor='center')


# Auto-Harvest control interface #
def button_harvest_callback():
    if label_harvest['text'] == 'Ready':
        label_harvest['text'] = 'Running'
        messagebox.showinfo('System_Status:', 'Harvest Now Running.')
    else:
        label_envr['text'] = 'Ready'


# label and button entities
label_harvest = tk.Label(master, text='Ready')
button_harvest = tk.Button(master, text='  Harvest   ', image=start_image, command=button_harvest_callback, compound=tk.TOP)

# label and button positions & plotting
label_harvest.place(relx=0.7, rely=0.6, anchor='center')
button_harvest.place(relx=0.4, rely=0.6, anchor='center')


# Universal kill-switch button interface #
def button_kill_callback():
    label_envr['text'] = 'Ready'
    label_harvest['text'] = 'Ready'
    messagebox.showinfo('System_Status:', 'Process Killed Successfully')


# label and button entities
button_kill = tk.Button(master, text='Kill Switch ', image=kill_image, command=button_kill_callback, compound=tk.TOP)
# label_kill = tk.Label(master, text=' ')

# label and button positions & plotting
# label_kill.grid(row=2, column=1)
button_kill.place(relx=0.4, rely=0.8, anchor='center')


# the app mainloop
tk.mainloop()

