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

checkbox_addition = tk.IntVar()
checkbox = tk.Checkbutton(window, text="+", variable=checkbox_addition, font=("Arial", 12))
checkbox.pack()

checkbox_subtraktion = tk.IntVar()
checkbox = tk.Checkbutton(window, text="-", variable=checkbox_subtraktion, font=("Arial", 12))
checkbox.pack()

checkbox_multiplikation = tk.IntVar()
checkbox = tk.Checkbutton(window, text="x", variable=checkbox_multiplikation, font=("Arial", 12))
checkbox.pack()

checkbox_division = tk.IntVar()
checkbox = tk.Checkbutton(window, text=":", variable=checkbox_division, font=("Arial", 12))
checkbox.pack()



# Create Numberspace


# run the main loop
window.mainloop()

#Classes

class Problem(window):
    defzahl=0 #placeholder