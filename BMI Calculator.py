import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.geometry("200x150")
win.resizable(0, 0)
win.configure(background="light grey")
win.title("BMI_Calculator")

#create lables

Height_lables = ttk.Label(win, text="enter your height")
Height_lables.grid(row=0, column=0, padx=4, pady=4)

Weight_lables = ttk.Label(win, text="enter your weght")
Weight_lables.grid(row=1, column=0, padx=4, pady=4)

result_lables = ttk.Label(win, text="Result: ")
result_lables.grid(row=3, column=0, padx=4, pady=4)

#create entry_box

Height_var  = tk.IntVar()
Height_entrybox = ttk.Entry(win, width=10, textvariable=Height_var)
Height_entrybox.grid(row=0, column=1, padx=4, pady=4)
Height_entrybox.focus()

Weight_var = tk.IntVar()
Weight_entrbox = ttk.Entry(win, width=10, textvariable=Weight_var)
Weight_entrbox.grid(row=1, column=1, padx=4, pady=4)

def action():
    user_height = Height_var.get()
    user_weight = Weight_var.get()

    BMI_var = ttk.Entry(win, width=14)
    BMI_var.grid(row=3, column=1)

    BMI = user_weight/(user_height/100)**2

    if BMI < 18.5:
        print("you r under_weight")

        BMI_var.insert(10, "Under_weight")

    if 18.5 <= BMI <= 24.9:
        print("Normal")

        BMI_var.insert(10, "Normal")

    if BMI > 24.9:

        BMI_var.insert(10, "Obese")

    print(f"devil is {user_height} cm heighted and his weight is {user_weight} kg.")

submit_button = ttk.Button(win, text="Submit", command=action)
submit_button.grid(row=2, column=0, padx=4, pady=4)
win.mainloop()