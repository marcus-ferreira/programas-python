# Banco de dados alimentícios

import tkinter as tk
import pandas as pd
from tkinter import ttk


class App:
    def __init__(self):
        window = tk.Tk()
        window.title("TacoDex")

        df = pd.read_csv("tacodex_db.csv")


        def choose():
            product = cbx_products.get()
            df_ = df.loc[df["Descrição"] == product]
            df_ = df_.iloc[0].to_string()
            lbl_text.config(text=f"{df_}", justify="right")


        # GUI
        df = df.sort_values(["Descrição"])

        frm_products = ttk.Frame(window)
        cbx_products = ttk.Combobox(frm_products, values=list(df["Descrição"].values), state="readonly", width=60)
        btn_choose = ttk.Button(frm_products, text="Escolher", command=choose)
        frm_data = ttk.Frame(window)
        lbl_text = ttk.Label(frm_data, text="Descrição\nTipo\nUmidade (%)\nEnergia (kcal)\nEnergia (kJ)\nProteína (g)\nLipídeos (g)\nColesterol (mg)\nCarboidrato (g)\nFibra Alimentar (g)\nCinzas (g)\nCálcio (mg)\nMagnésio (mg)\nManganês (mg)\nFósforo (mg)\nFerro (mg)\nSódio (mg)\nPotássio (mg)\nCobre (mg)\nZinco (mg)\nRetinol (mcg)\nRE (mcg)\nRAE (mcg)\nTiamina (mg)\nRiboflavina (mg)\nPiridoxina (mg)\nNiacina (mg)\nVitamina C (mg)")

        frm_products.grid(row=0, padx=10, pady=10)
        cbx_products.grid(row=0)
        btn_choose.grid(row=0, column=2, sticky="e")
        frm_data.grid(row=1, padx=10, pady=10, sticky="w")
        lbl_text.grid(row=0)

        window.mainloop()

App()
