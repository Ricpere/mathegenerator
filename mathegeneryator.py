#Import Module
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#

#Define Variables
additionrechnen = True
subtraktionrechnen = True
multiplikationrechnen = True
divisionrechnen = True
result = 0
rechnung = 0

#generate Math Calculation



def generate_problem(*args):

    #Generate Nummbers
    num1= random.randint(1, 20)
    num2= random.randint(1, 20)

    #chose Operations

    operations = []
    if additionrechnen == True:
        operations.append ("addition")
    if subtraktionrechnen == True:
        operations.append ("subtraktion")
    if multiplikationrechnen == True:
        operations.append ("multiplikation")
    if divisionrechnen == True:
        operations.append ("division")

    global result
    global rechnung

    chosen_operation = random.choice(operations)
    if chosen_operation == "addition":
        result = num1 + num2
        rechnung= "%i + %i" %(num1, num2)
    if chosen_operation == "subtraktion":
        result = num1 - num2
        rechnung= "%i - %i" %(num1, num2)
    if chosen_operation == "multiplikation":
        result = num1 * num2
        rechnung= "%i * %i" %(num1, num2)
    if chosen_operation == "division":
        tempresultat= num1 * num2
        result = tempresultat / num1
        rechnung= "%i : %i" %(tempresultat, num1)

generate_problem()
#generate window and optics

#Mainframe
window= tk.Tk()
window.title ("Kofprechnen macht Spass!")

# create the problem label title
problem_label_title = tk.Label(text="Rechenaufgabe:", font=("Arial", 24))
problem_label_title.pack()

# create the problem 
problem = tk.Label(text= rechnung, font=("Arial", 24))
problem.pack()

# create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24))
answer_entry.pack()

#Create Submitbutton

answer_button = tk.Button(text= "Resultat Prüfen", font=("Arial", 12),)
answer_button.pack()

# Create a checkbox

checkbox_addition = tk.IntVar()
checkbox = tk.Checkbutton(window, text="+", variable=checkbox_addition, font=("Arial", 12))
checkbox_addition.set(True)
checkbox.pack()

checkbox_subtraktion = tk.IntVar()
checkbox = tk.Checkbutton(window, text="-", variable=checkbox_subtraktion, font=("Arial", 12))
checkbox_subtraktion.set(True)
checkbox.pack()

checkbox_multiplikation = tk.IntVar()
checkbox = tk.Checkbutton(window, text="x", variable=checkbox_multiplikation, font=("Arial", 12),)
checkbox_multiplikation.set(True)
checkbox.pack()

checkbox_division = tk.IntVar()
checkbox = tk.Checkbutton(window, text=":", variable=checkbox_division, font=("Arial", 12))
checkbox_division.set(True)
checkbox.pack()

def update_operations(*args):
   
    # Enable or disable the operations based on the checkbox values
    if checkbox_addition.get() == 1 :
        additionrechnen = True
        print ("Additionsrechnen an")
    else:
        additionrechnen = False
        print ("Additionsrechnen aus")

    if checkbox_subtraktion.get() == 1:
        subtraktionrechnen = True
        print ("Subtraktionsrechnen an")
    else:
        subtraktionrechnen = False
        print ("Subtraktionsrechnen aus")

    if checkbox_multiplikation.get() == 1:
        multiplikationrechnen = True
        print ("Multiplikationsrechnen an")
    else:
        multiplikationrechnen = False
        print ("Multiplikationsrechnen aus")

    if checkbox_division.get() == 1:
       divisionrechnen = True
       print ("Divisionsrechnen an")
    else:
        divisionrechnen = False
        print (divisionrechnen)
        print ("Divisionsrechnen aus")
    


# Call the update_operations function whenever a checkbox is clicked
checkbox_addition.trace("w", update_operations)
checkbox_subtraktion.trace("w", update_operations)
checkbox_multiplikation.trace("w", update_operations)
checkbox_division.trace("w", update_operations)

#print(update_operations)
# Create Numberspace


# run the main loop
window.mainloop()
