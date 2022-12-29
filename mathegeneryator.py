#Import Module
import random
import tkinter as tk
from tkinter import ttk


#generate window and optics

#Mainframe
window= tk.Tk()
window.title ("Kofprechnen macht Spass!")

# create the problem label
problem_label = tk.Label(text="Rechenaufgabe:", font=("Arial", 24))
problem_label.pack()

# create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24))
answer_entry.pack()

# Create a checkbox
checkbox_value = tk.IntVar()
checkbox = tk.Checkbutton(window, text="Option", variable=checkbox_value, font=("Arial", 24))
checkbox.pack()

# Create Numberspace


# run the main loop
window.mainloop()

#Classes

class Problem(window):
    defzahl=0 #placeholder