# Contagem de Pesquisas #

import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.create_window()

    def create_window(self):
        def adicionar():
            try: 
                if r1.get() != 0 and r2.get() != 0 and r3.get() != 0:
                    if r1.get() == 1:
                        q1["Muito bom"] += 1
                    elif r1.get() == 2:
                        q1["Bom"] += 1
                    elif r1.get() == 3:
                        q1["Regular"] += 1
                    elif r1.get() == 4:
                        q1["Ruim"] += 1

                    if r2.get() == 1:
                        q2["Muito bom"] += 1
                    elif r2.get() == 2:
                        q2["Bom"] += 1
                    elif r2.get() == 3:
                        q2["Regular"] += 1
                    elif r2.get() == 4:
                        q2["Ruim"] += 1

                    if r3.get() == 1:
                        q3["Sim"] += 1
                    elif r3.get() == 2:
                        q3["Não"] += 1

                    text_resultado.config(text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")
                else:
                    text_resultado.config(text="Escolha os valores corretamente!")
            except:
                text_resultado.config(text="Escolha os valores corretamente!")

        def limpar():
            q1["Muito bom"], q1["Bom"], q1["Regular"], q1["Ruim"] = 0, 0, 0, 0
            q2["Muito bom"], q2["Bom"], q2["Regular"], q2["Ruim"] = 0, 0, 0, 0
            q3["Sim"], q3["Não"] = 0, 0
            r1.set(None)
            r2.set(None)
            r3.set(None)
            text_resultado.config(text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")

        window = tk.Tk()
        window.title("Contagem de Pesquisas")

        q1 = {"Muito bom": 0, "Bom": 0, "Regular": 0, "Ruim": 0}
        q2 = {"Muito bom": 0, "Bom": 0, "Regular": 0, "Ruim": 0}
        q3 = {"Sim": 0, "Não": 0}
        r1 = tk.IntVar()
        r2 = tk.IntVar()
        r3 = tk.IntVar()

        label_q1 = tk.Label(window, text="Como você classifica o atendimento médico da clínica?")
        label_q1.grid(row=0, column=0, columnspan=2)
        radio_q1_r1 = tk.Radiobutton(window, text="Muito bom", variable=r1, value=1)
        radio_q1_r1.grid(row=1, column=0)
        radio_q1_r2 = tk.Radiobutton(window, text="Bom", variable=r1, value=2)
        radio_q1_r2.grid(row=1, column=1)
        radio_q1_r3 = tk.Radiobutton(window, text="Regular", variable=r1, value=3)
        radio_q1_r3.grid(row=2, column=0)
        radio_q1_r4 = tk.Radiobutton(window, text="Ruim", variable=r1, value=4)
        radio_q1_r4.grid(row=2, column=1)

        label_q2 = tk.Label(window, text="Como você classifica as instalações da clínica com relação ao espaço físico e conforto?")
        label_q2.grid(row=3, column=0, columnspan=2)
        radio_q2_r1 = tk.Radiobutton(window, text="Muito bom", variable=r2, value=1)
        radio_q2_r1.grid(row=4, column=0)
        radio_q2_r2 = tk.Radiobutton(window, text="Bom", variable=r2, value=2)
        radio_q2_r2.grid(row=4, column=1)
        radio_q2_r3 = tk.Radiobutton(window, text="Regular", variable=r2, value=3)
        radio_q2_r3.grid(row=5, column=0)
        radio_q2_r4 = tk.Radiobutton(window, text="Ruim", variable=r2, value=4)
        radio_q2_r4.grid(row=5, column=1)

        label_q3 = tk.Label(window, text="Você recomendaria a clínica para colegas de trabalho ou outras empresas?")
        label_q3.grid(row=6, column=0, columnspan=2)
        radio_q3_r1 = tk.Radiobutton(window, text="Sim", variable=r3, value=1)
        radio_q3_r1.grid(row=7, column=0)
        radio_q3_r2 = tk.Radiobutton(window, text="Não", variable=r3, value=2)
        radio_q3_r2.grid(row=7, column=1)

        text_resultado = tk.Label(window, text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")
        text_resultado.grid(row=0, column=2, rowspan=10)

        button_adicionar = tk.Button(window, text="Adicionar", command=adicionar)
        button_adicionar.grid(row=8, column=0)
        button_limpar = tk.Button(window, text="Limpar", command=limpar)
        button_limpar.grid(row=8, column=1)

        window.mainloop()

App()
