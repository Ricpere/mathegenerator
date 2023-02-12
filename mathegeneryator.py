"""""
© Dario Bertozzi & Ricardo Pereira 

Versionslog:
V.01 Erstellen der Funktionen und generierung der Rechenaufgabe. Implementierung der Update Checkboxes Funktion.
V0.2 Erstellung des GUIS
V0.3 Dynamisches GUI mit aktualisierung der Rechnung
V0.4 Implementierung des Aufgaben prüfen buttons und der funktionalität dahinter
V0.5 Bugfixes gemäss Testsprint 1 (Anpassung der Variablen auf Global)
V0.6 Generallüberarbeitung GUI

"""


# Import Module
import random
import tkinter as tk
from tkinter import messagebox

#New Gui
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x400")
window.title("Kofprechnen macht Spass!")

problem_label_title = tk.Label(text="Rechenaufgabe:", font=("Arial", 24), width=21)
problem_label_title.grid(row=0, column=0, sticky="")


#create the problem
problem = tk.Label(text="rechnung", font=("Arial", 24), width=0)                     #Rechnung anpassen
problem.grid(row=1, column=0)


#create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24), width=9)
answer_entry.grid(row=2, column=0)


#create/position button Prüfen
answer_button = tk.Button(text="Prüfen", font=("Arial", 14))
answer_button.grid(row=3, column=0)


#create/position button Neue Aufgabe
answer_button = tk.Button(text="Neue Aufgabe", font=("Arial", 12))
answer_button.place(x=60, y=190)


#create button 9
one_button = tk.Button(text="9", font=("Arial", 14))
one_button.place(x=315, y=190)

#create button 8
one_button = tk.Button(text="8", font=("Arial", 14))
one_button.place(x=275, y=190)

#create button 7
one_button = tk.Button(text="7", font=("Arial", 14))
one_button.place(x=235, y=190)

#create button 6
one_button = tk.Button(text="6", font=("Arial", 14))
one_button.place(x=315, y=240)

#create button 5
one_button = tk.Button(text="5", font=("Arial", 14))
one_button.place(x=275, y=240)

#create button 4
one_button = tk.Button(text="4", font=("Arial", 14))
one_button.place(x=235, y=240)

#create button 3
one_button = tk.Button(text="3", font=("Arial", 14))
one_button.place(x=315, y=290)

#create button 2
one_button = tk.Button(text="2", font=("Arial", 14))
one_button.place(x=275, y=290)

#create button 1
one_button = tk.Button(text="1", font=("Arial", 14))
one_button.place(x=235, y=290)

#create button 0
one_button = tk.Button(text="0", font=("Arial", 14))
one_button.place(x=235, y=340)

#create button Enter
one_button = tk.Button(text="Enter", font=("Arial", 14))
one_button.place(x=275, y=340)


####create and set default status for radiobutton
selected_option =  tk.StringVar()
selected_option.set("easy")

#create radiobutton easy
easy_option = tk.Radiobutton(text="Easy", variable=selected_option, value="easy")
easy_option.place(x=60, y=240)

#create radiobutton hard
hard_option = tk.Radiobutton(text="Hard", variable=selected_option, value="hard")
hard_option.place(x=60, y=280)


####create and set default status for checkboxes
checkbox_subtraction = tk.IntVar()
checkbox_addition = tk.IntVar()
checkbox_division = tk.IntVar()
checkbox_multiplikation = tk.IntVar()

#create checkbox multiplication
checkbox = tk.Checkbutton(text="*",variable=checkbox_multiplikation, font=("Arial", 16))
checkbox.place(x=60, y=320)
checkbox_multiplikation.set(True)

#create checkbox division
checkbox = tk.Checkbutton(text=":",variable=checkbox_division, font=("Arial", 16))
checkbox.place(x=100, y=320)
checkbox_division.set(True)

#create checkbox subtraction
checkbox = tk.Checkbutton(text="-", variable=checkbox_subtraction, font=("Arial", 16),)
checkbox.place(x=140, y=320)
checkbox_subtraction.set(True)

#create checkbox addition
checkbox = tk.Checkbutton(text="+", variable=checkbox_addition , font=("Arial", 16))
checkbox.place(x=180, y=320)
checkbox_addition.set(True)

window.mainloop()
"""
# Define Variables
additionrechnen = True
subtraktionrechnen = True
multiplikationrechnen = True
divisionrechnen = True
result = int(0)
rechnung = int(0)
user_answer = False
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)

# generate Numbers


def generate_number():
    global num1
    global num2
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
# generate Math Calculation


def generate_problem(*args):

    # chose Operations

    operations = []
    if additionrechnen == True:
        operations.append("addition")
    if subtraktionrechnen == True:
        operations.append("subtraktion")
    if multiplikationrechnen == True:
        operations.append("multiplikation")
    if divisionrechnen == True:
        operations.append("division")

    global result
    global rechnung

    chosen_operation = random.choice(operations)
    if chosen_operation == "addition":
        result = num1 + num2
        rechnung = "%i + %i" % (num1, num2)
    if chosen_operation == "subtraktion":
        result = num1 - num2
        rechnung = "%i - %i" % (num1, num2)
    if chosen_operation == "multiplikation":
        result = num1 * num2
        rechnung = "%i * %i" % (num1, num2)
    if chosen_operation == "division":
        tempresultat = num1 * num2
        result = tempresultat / num1
        rechnung = "%i : %i" % (tempresultat, num1)


# generate Problem

generate_problem()


# generate window and optics

# Mainframe
window = tk.Tk()
window.resizable(False, False)
window.title("Kofprechnen macht Spass!")


# create the problem label title
problem_label_title = tk.Label(text="Rechenaufgabe:", font=("Arial", 24))
problem_label_title.grid(row=0, column=0)

# create the problem
problem = tk.Label(text=rechnung, font=("Arial", 24))
problem.grid(row=1, column=0)

# create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24),)
answer_entry.grid(row=2, column=0)

# Create Submitbutton and the logic of it


def check_answer():
    update_operations()
    global rechnung
    global result
    global user_answer
    user_answer = int(answer_entry.get())
    if user_answer == result:
        print("Rechnung richtig")
        print("Input=", user_answer)
        print("Resultat=", result)
        generate_number()
        generate_problem()

        problem.config(text=rechnung)

        return True

    else:
        print("Rechnung falsch")
        print("Input=", user_answer)
        print("Resultat=", result)
        return False


answer_button = tk.Button(text="Resultat Prüfen", font=(
    "Arial", 12), command=check_answer)
answer_button.grid(row=3, column=0)


# frame
frame = tk.Frame(window, borderwidth=0, relief="solid")
frame.grid(row=4, column=0)

# Create a checkbox

checkbox_addition = tk.IntVar()
checkbox = tk.Checkbutton(
    frame, text="+", variable=checkbox_addition, font=("Arial", 12))
checkbox_addition.set(True)
checkbox.grid(row=4, column=0)
# checkbox.pack()

checkbox_subtraktion = tk.IntVar()
checkbox = tk.Checkbutton(
    frame, text="-", variable=checkbox_subtraktion, font=("Arial", 12))
checkbox_subtraktion.set(True)
checkbox.grid(row=4, column=1, padx=5, pady=5)
# checkbox.pack()

checkbox_multiplikation = tk.IntVar()
checkbox = tk.Checkbutton(
    frame, text="x", variable=checkbox_multiplikation, font=("Arial", 12),)
checkbox_multiplikation.set(True)
checkbox.grid(row=4, column=2, padx=5, pady=5)
# checkbox.pack()

checkbox_division = tk.IntVar()
checkbox = tk.Checkbutton(
    frame, text=":", variable=checkbox_division, font=("Arial", 12))
checkbox_division.set(True)
checkbox.grid(row=4, column=3, padx=5, pady=5)
# checkbox.pack()

window.columnconfigure(0, pad=60)
window.columnconfigure(1, pad=60)
window.columnconfigure(2, pad=60)
window.columnconfigure(3, pad=60)


def update_operations(*args):

    global additionrechnen
    global subtraktionrechnen
    global divisionrechnen
    global multiplikationrechnen
    # Enable or disable the operations based on the checkbox values
    if checkbox_addition.get() == 1:
        additionrechnen = True
        print("Additionsrechnen an")
    else:
        additionrechnen = False
        print("Additionsrechnen aus")

    if checkbox_subtraktion.get() == 1:
        subtraktionrechnen = True
        print("Subtraktionsrechnen an")
    else:
        subtraktionrechnen = False
        print("Subtraktionsrechnen aus")

    if checkbox_multiplikation.get() == 1:
        multiplikationrechnen = True
        print("Multiplikationsrechnen an")
    else:
        multiplikationrechnen = False
        print("Multiplikationsrechnen aus")

    if checkbox_division.get() == 1:
       divisionrechnen = True
       print("Divisionsrechnen an")
    else:
        divisionrechnen = False
        print(divisionrechnen)
        print("Divisionsrechnen aus")


# Call the update_operations function whenever a checkbox is clicked
checkbox_addition.trace("w", update_operations)
checkbox_subtraktion.trace("w", update_operations)
checkbox_multiplikation.trace("w", update_operations)
checkbox_division.trace("w", update_operations)

# print(update_operations)
# Create Numberspace


# run the main loop
window.mainloop()
"""