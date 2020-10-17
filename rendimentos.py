import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        # Functions
        def calculate():
            present_value = float(entry1.get())
            tax = float(entry2.get()) / 100
            time = int(entry3.get())
            future_value = float(present_value * ((1 + tax) ** time))
            resultado.config(text=f"O valor a ser recebido será de R$ {round(future_value, 2)}")


        # GUI
        window = tk.Tk()
        window.title("Cálculo de Rendimentos")

        label1 = tk.Label(window, text="Qual o valor da aplicação?")
        entry1 = tk.Entry(window)
        label2 = tk.Label(window, text="Qual a taxa de juros? (a.m. em %)")
        entry2 = tk.Entry(window)
        label3 = tk.Label(window, text="Qual o tempo da aplicação em meses?")
        entry3 = tk.Entry(window)
        button1 = tk.Button(window, text="Calcular", command=calculate)
        resultado = tk.Label(window, text="")


        # Grid
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        label3.grid(row=2, column=0)
        entry3.grid(row=2, column=1)
        button1.grid(row=3, column=0, columnspan=2)
        resultado.grid(row=4, column=0, columnspan=2)


        window.mainloop()

# Initiate program
App()
