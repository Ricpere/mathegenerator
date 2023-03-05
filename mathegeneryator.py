"""""
© Dario Bertozzi & Ricardo Pereira

Versionslog:
V.01 Erstellen der Funktionen und generierung der Rechenaufgabe. Implementierung der Update Checkboxes Funktion.
V0.2 Erstellung des GUIS
V0.3 Dynamisches GUI mit aktualisierung der Rechnung
V0.4 Implementierung des Aufgaben prüfen buttons und der funktionalität dahinter
V0.5 Bugfixes gemäss Testsprint 1 (Anpassung der Variablen auf Global)
V0.6 Implementierung der Automatischen Lösungskontrolle im Gui inklusive Eingabelöschung.
Implementierung der neue Aufgabe Funkion
Implementierung der Schwierigkeit
V0.7 Anpassung gemäss Testsprint 2 (Anpassung des Guis und Steigerung der Schwierigkeit auf Stufe Schwer)
V0.8 Anpassung gemäss Testsprint 3 (Hinzufügen der Minustaste bei der Eingabe auf dem Bildschirm)
"""

# Import Module
import random
import tkinter as tk
from tkinter import messagebox

# Define Variables
additionrechnen = True
subtraktionrechnen = True
multiplikationrechnen = True
divisionrechnen = True
result = int(0)
rechnung = int(0)
user_answer = False
problem = "1"

# New Gui
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x400")
window.title("Kofprechnen macht Spass!")

problem_label_title = tk.Label(text="Rechenaufgabe:", font=("Arial", 24), width=21)
problem_label_title.grid(row=0, column=0, sticky="")

# create the problem
problem = tk.Label(text=rechnung, font=("Arial", 24), width=0)  # Rechnung anpassen
problem.grid(row=1, column=0)

# create the answer entry field
answer_entry = tk.Entry(font=("Arial", 24), width=9)
answer_entry.grid(row=2, column=0)
answer_entry.focus()


# create/position button Neue Aufgabe and the logic of it.

def NeueAufgabe():
    generate_problem()


answer_button = tk.Button(text="Neue Aufgabe", font=("Arial", 12), command=NeueAufgabe)
answer_button.place(x=60, y=190)


# create button 9
def insert_number9():
    answer_entry.insert(tk.END, "9")


one_button = tk.Button(text="9", font=("Arial", 14), command=insert_number9)
one_button.place(x=315, y=190)


# create button 8
def insert_number8():
    answer_entry.insert(tk.END, "8")


one_button = tk.Button(text="8", font=("Arial", 14), command=insert_number8)
one_button.place(x=275, y=190)


# create button 7
def insert_number7():
    answer_entry.insert(tk.END, "7")


one_button = tk.Button(text="7", font=("Arial", 14), command=insert_number7)
one_button.place(x=235, y=190)


# create button 6
def insert_number6():
    answer_entry.insert(tk.END, "6")


one_button = tk.Button(text="6", font=("Arial", 14), command=insert_number6)
one_button.place(x=315, y=240)


# create button 5
def insert_number5():
    answer_entry.insert(tk.END, "5")


one_button = tk.Button(text="5", font=("Arial", 14), command=insert_number5)
one_button.place(x=275, y=240)


# create button 4
def insert_number4():
    answer_entry.insert(tk.END, "4")


one_button = tk.Button(text="4", font=("Arial", 14), command=insert_number4)
one_button.place(x=235, y=240)


# create button 3
def insert_number3():
    answer_entry.insert(tk.END, "3")


one_button = tk.Button(text="3", font=("Arial", 14), command=insert_number3)
one_button.place(x=315, y=290)


# create button 2
def insert_number2():
    answer_entry.insert(tk.END, "2")


one_button = tk.Button(text="2", font=("Arial", 14), command=insert_number2)
one_button.place(x=275, y=290)


# create button 1
def insert_number1():
    answer_entry.insert(tk.END, "1")


one_button = tk.Button(text="1", font=("Arial", 14), command=insert_number1)
one_button.place(x=235, y=290)


# create button 0
def insert_number0():
    answer_entry.insert(tk.END, "0")


one_button = tk.Button(text="0", font=("Arial", 14), command=insert_number0)
one_button.place(x=235, y=340)

# create button -
def insert_minus():
    answer_entry.insert(tk.END, "-")


one_button = tk.Button(text="-", font=("Arial", 14), command=insert_minus)
one_button.place(x=345, y=340)

####create and set default status for radiobutton
easy_mode = tk.BooleanVar(value=True)
# easy_mode.set(True) #zerstört die Variable für das Programm

# create radiobutton easy
easy_option = tk.Radiobutton(text="Einfach", variable=easy_mode, value=True)
easy_option.place(x=60, y=240)

# create radiobutton hard
hard_option = tk.Radiobutton(text="Schwer", variable=easy_mode, value=False)
hard_option.place(x=60, y=280)

####create and set default status for checkboxes
checkbox_subtraction = tk.IntVar()
checkbox_addition = tk.IntVar()
checkbox_division = tk.IntVar()
checkbox_multiplikation = tk.IntVar()

# create checkbox multiplication
checkbox = tk.Checkbutton(text="x", variable=checkbox_multiplikation, font=("Arial", 16))
checkbox.place(x=60, y=320)
checkbox_multiplikation.set(True)

# create checkbox division
checkbox = tk.Checkbutton(text=":", variable=checkbox_division, font=("Arial", 16))
checkbox.place(x=100, y=320)
checkbox_division.set(True)

# create checkbox subtraction
checkbox = tk.Checkbutton(text="-", variable=checkbox_subtraction, font=("Arial", 16), )
checkbox.place(x=140, y=320)
checkbox_subtraction.set(True)

# create checkbox addition
checkbox = tk.Checkbutton(text="+", variable=checkbox_addition, font=("Arial", 16))
checkbox.place(x=180, y=320)
checkbox_addition.set(True)


def generate_numbers():
    global easy_mode
    global num1
    global num2

    if easy_mode.get() == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print("easy")
    else:

        num1 = random.randint(5, 20)
        num2 = random.randint(5, 20)
        print("hard")
    return num1, num2


def generate_problem(*args):
    generate_numbers()

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

    global easy_mode
    global result
    global rechnung
    global num1
    global num2

    chosen_operation = random.choice(operations)
    if chosen_operation == "addition":
        result = num1 + num2
        rechnung = "%i + %i" % (num1, num2)
    if chosen_operation == "subtraktion":
        result = num1 - num2
        rechnung = "%i - %i" % (num1, num2)
    if chosen_operation == "multiplikation":
        result = num1 * num2
        rechnung = "%i x %i" % (num1, num2)
    if chosen_operation == "division":
        tempresultat = num1 * num2
        result = tempresultat / num1
        rechnung = "%i : %i" % (tempresultat, num1)
    problem.config(text=rechnung)
    answer_entry.delete(0, tk.END)
    return result, rechnung, num1, num2


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

    if checkbox_subtraction.get() == 1:
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
checkbox_subtraction.trace("w", update_operations)
checkbox_multiplikation.trace("w", update_operations)
checkbox_division.trace("w", update_operations)


# create/position button Prüfen

def check_answer(*args):
    update_operations()
    global rechnung
    global result
    global user_answer

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Falsch :(")
        window.after(1000, lambda: answer_entry.delete(0, tk.END))
        return False

    if user_answer == result:
        print("Rechnung richtig")
        print("Input=", user_answer)
        print("Resultat=", result)
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Richtig :-)")
        window.after(1000, generate_problem)

        return True

    else:
        print("Rechnung falsch")
        print("Input=", user_answer)
        print("Resultat=", result)
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "FALSCH :-(")
        window.after(1000, lambda: answer_entry.delete(0, tk.END))
        return False


answer_button = tk.Button(text="Prüfen", font=("Arial", 14), command=check_answer)
answer_button.grid(row=3, column=0)

# create button Enter
one_button = tk.Button(text="Enter", font=("Arial", 14), command=check_answer)
one_button.place(x=275, y=340)
answer_entry.bind('<Return>', check_answer)

# generate Rechnung on Startup
generate_problem()

# Bind the "Enter" Key


window.mainloop()
