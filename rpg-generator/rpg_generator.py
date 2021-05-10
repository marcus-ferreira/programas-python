import tkinter as tk
import pandas as pd
import random
from tkinter import ttk

class App:
    def __init__(self):
        # Functions
        def generate():
            df = pd.read_csv("db.csv")
            goal = df["Objetivo"][random.randint(0, 35)]
            location = df["Local"][random.randint(0, 35)]
            villain = df["Vilão"][random.randint(0, 35)]
            ally = df["Aliado"][random.randint(0, 35)]
            complication = df["Complicação"][random.randint(0, 35)]
            lbl_result.config(text=f"Objetivo: {goal}\nLocal: {location}\nVilão: {villain}\nAliado(s): {ally}\nComplicação: {complication}")

        # Gui
        window = tk.Tk()
        window.title("Gerador de Aventuras RPG")
        window.config(padx=10, pady=10)

        lbl_title = ttk.Label(window, text="Gerador de Aventuras", font="Helvetica 20 bold")
        btn_generate = ttk.Button(window, text="Gerar", command=generate)
        lbl_result = ttk.Label(window)

        lbl_title.grid(row=0)
        btn_generate.grid(row=1)
        lbl_result.grid(row=2, sticky="w")

        window.mainloop()

App()
