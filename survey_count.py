import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        # Functions
        def add(r1, r2, r3):
            try: 
                if r1 != 0 and r2 != 0 and r3 != 0:
                    q1[r1 - 1][1] += 1
                    q2[r2 - 1][1] += 1
                    q3[r3 - 1][1] += 1
                    text_resultado.config(text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")
                else:
                    text_resultado.config(text="Escolha os valores corretamente!")
            except:
                text_resultado.config(text="Escolha os valores corretamente!")

        def clear():
            q1[0][1], q1[1][1], q1[2][1], q1[3][1] = 0, 0, 0, 0
            q2[0][1], q2[1][1], q2[2][1], q2[3][1] = 0, 0, 0, 0
            q3[0][1], q3[1][1] = 0, 0
            r1.set(None)
            r2.set(None)
            r3.set(None)
            text_resultado.config(text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")


        # GUI
        window = tk.Tk()
        window.title("Contagem de Pesquisas")

        q1 = [["Muito bom", 0], ["Bom", 0], ["Regular", 0], ["Ruim", 0]]
        q2 = [["Muito bom", 0], ["Bom", 0], ["Regular", 0], ["Ruim", 0]]
        q3 = [["Sim", 0], ["Não", 0]]
        r1 = tk.IntVar()
        r2 = tk.IntVar()
        r3 = tk.IntVar()

        lbl_frame1 = tk.LabelFrame(window)
        label_q1 = tk.Label(lbl_frame1, text="Como você classifica o atendimento médico da clínica?")
        radio_q1_r1 = tk.Radiobutton(lbl_frame1, text="Muito bom", variable=r1, value=1)
        radio_q1_r2 = tk.Radiobutton(lbl_frame1, text="Bom", variable=r1, value=2)
        radio_q1_r3 = tk.Radiobutton(lbl_frame1, text="Regular", variable=r1, value=3)
        radio_q1_r4 = tk.Radiobutton(lbl_frame1, text="Ruim", variable=r1, value=4)
        label_q2 = tk.Label(lbl_frame1, text="Como você classifica as instalações da clínica com relação ao espaço físico e conforto?")
        radio_q2_r1 = tk.Radiobutton(lbl_frame1, text="Muito bom", variable=r2, value=1)
        radio_q2_r2 = tk.Radiobutton(lbl_frame1, text="Bom", variable=r2, value=2)
        radio_q2_r3 = tk.Radiobutton(lbl_frame1, text="Regular", variable=r2, value=3)
        radio_q2_r4 = tk.Radiobutton(lbl_frame1, text="Ruim", variable=r2, value=4)
        label_q3 = tk.Label(lbl_frame1, text="Você recomendaria a clínica para colegas de trabalho ou outras empresas?")
        radio_q3_r1 = tk.Radiobutton(lbl_frame1, text="Sim", variable=r3, value=1)
        radio_q3_r2 = tk.Radiobutton(lbl_frame1, text="Não", variable=r3, value=2)

        lbl_frame2 = tk.LabelFrame(window)
        text_resultado = tk.Label(lbl_frame2, text=f"Como você classifica o atendimento médico da clínica?\n{q1}\n\nComo você classifica as instalações da clínica com relação ao espaço físico e conforto?\n{q2}\n\nVocê recomendaria a clínica para colegas de trabalho ou outras empresas?\n{q3}\n")

        button_add = tk.Button(window, text="Adicionar", command=lambda: add(r1.get(), r2.get(), r3.get()))
        button_clear = tk.Button(window, text="Limpar", command=clear)


        # Grid
        lbl_frame1.grid(row=0, column=0, padx=10, pady=10)
        label_q1.grid(row=0, column=0, sticky="w")
        radio_q1_r1.grid(row=1, column=0, sticky="w")
        radio_q1_r2.grid(row=2, column=0, sticky="w")
        radio_q1_r3.grid(row=3, column=0, sticky="w")
        radio_q1_r4.grid(row=4, column=0, sticky="w")
        label_q2.grid(row=5, column=0, sticky="w")
        radio_q2_r1.grid(row=6, column=0, sticky="w")
        radio_q2_r2.grid(row=7, column=0, sticky="w")
        radio_q2_r3.grid(row=8, column=0, sticky="w")
        radio_q2_r4.grid(row=9, column=0, sticky="w")
        label_q3.grid(row=10, column=0, sticky="w")
        radio_q3_r1.grid(row=11, column=0, sticky="w")
        radio_q3_r2.grid(row=12, column=0, sticky="w")

        lbl_frame2.grid(row=0, column=1, padx=10, pady=10)
        text_resultado.grid(row=0, column=0)
 
        button_add.grid(row=1, column=0, padx=10, pady=10)
        button_clear.grid(row=1, column=1, padx=10, pady=10)


        window.mainloop()


App()
