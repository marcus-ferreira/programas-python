# Cálculo de Rendimentos

import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.create_window()

    def create_window(self):
        window = tk.Tk()
        window.title("Cálculo de Rendimentos")

        label1 = tk.Label(window, text="Qual o valor da aplicação?")
        label1.pack()
        entry1 = tk.Entry(window)
        entry1.pack()

        label2 = tk.Label(window, text="Qual a taxa de juros? (a.m. em %)")
        label2.pack()
        entry2 = tk.Entry(window)
        entry2.pack()

        label3 = tk.Label(window, text="Qual o tempo da aplicação em meses?")
        label3.pack()
        entry3 = tk.Entry(window)
        entry3.pack()

        resultado = tk.Label(window, text="")
        resultado.pack()

        def calcular():
            vp = float(entry1.get())
            j = float(entry2.get()) / 100
            n = int(entry3.get())
            vf = float(vp * ((1 + j) ** n))

            resultado.config(text=f"O valor a ser recebido será de R$ {round(vf, 2)}")

        button1 = tk.Button(window, text="Calcular", command=calcular)
        button1.pack()

        window.mainloop()

App()
