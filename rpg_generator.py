import tkinter as tk
import pandas as pd
import random
from tkinter import ttk


class App:
    def __init__(self):
        # Functions
        def generate():
            goal = df["Objetivo"][random.randint(0, 35)]
            location = df["Local"][random.randint(0, 35)]
            villain = df["Vilão"][random.randint(0, 35)]
            ally = df["Aliado"][random.randint(0, 35)]
            complication = df["Complicação"][random.randint(0, 35)]
            lbl_result.config(text=f"Objetivo: {goal}\nLocal: {location}\nVilão: {villain}\nAliado(s): {ally}\nComplicação: {complication}")
        

        df = pd.read_csv("db.csv")


        # Gui
        window = tk.Tk()
        window.title("Ajuda RPG")
        window.resizable(False, False)

        lbl_title = ttk.Label(window, text="Gerador de Aventuras", font="Helvetica 20 bold")
        btn_generate = ttk.Button(window, text="Gerar", command=generate)
        lbl_result = ttk.Label(window)


        # Grid
        lbl_title.grid(row=0)
        btn_generate.grid(row=1)
        lbl_result.grid(row=2)


        window.mainloop()


App()
