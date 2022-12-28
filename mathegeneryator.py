#Import Module
import random
import tkinter as tk
from tkinter import ttk

#generate window and optics

#Mainframe
window= tk.Tk()
window.title ("Rechenaufgabe:")

# create the problem label
problem_label = tk.Label(text="Rechenaufgabe:", font=("Arial", 24))
problem_label.pack()

# create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24))
answer_entry.pack()


# run the main loop
window.mainloop()