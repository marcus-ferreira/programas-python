import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App:
    def __init__(self):
        # Functions
        def calculate():
            last_reading = float(entry1.get())
            actual_reading = float(entry2.get())
            kwh_spent = actual_reading - last_reading
            public_lighting = 7.8

            if 0 < kwh_spent <= 30:
                green_flag_price = kwh_spent * 0.26 + public_lighting
                yellow_flag_price = 0
                red_flag_price = kwh_spent * 0.33 + public_lighting
            elif 31 < kwh_spent <= 100:
                green_flag_price = 30 * 0.26 + (kwh_spent - 30) * 0.45 + public_lighting
                yellow_flag_price = 0
                red_flag_price = 30 * 0.33 + (kwh_spent - 30) * 0.52 + public_lighting
            else:
                green_flag_price = 30 * 0.26 + 70 * 0.45 + (kwh_spent - 100) * 0.67 + public_lighting
                yellow_flag_price = 0
                red_flag_price = 30 * 0.33 + 70 * 0.52 + (kwh_spent - 100) * 0.74 + public_lighting

            resultado.config(text=f"Valor estimado a pagar:\nBandeira Verde: R$ {round(green_flag_price, 2)}\nBandeira Amarela: R$ {round(yellow_flag_price, 2)}\nBandeira Vermelha: R$ {round(red_flag_price, 2)}")


        # GUI
        window = tk.Tk()
        window.title("Cálculo de Luz")
        window.iconbitmap("light-icon.ico")


        logo = ImageTk.PhotoImage(Image.open("light-logo.png").resize((150, 55)))
        label_logo = tk.Label(window, image=logo)

        block1= tk.LabelFrame(window, bd=0)
        label1 = tk.Label(block1, text="Última medição", fg="#636363")
        entry1 = tk.Entry(block1, width=30)

        block2 = tk.LabelFrame(window, bd=0)
        label2 = tk.Label(block2, text="Medição atual", fg="#636363")
        entry2 = tk.Entry(block2, width=30)

        block3 = tk.LabelFrame(window, bd=0)
        button = tk.Button(block3, text="CALCULAR", command=calculate, bg="#FFBB75", fg="white", activebackground="#E28728", activeforeground="white", width=25, height=2, relief="flat")
        resultado = tk.Label(window, text="")

        # Grid
        window.config(padx=80)

        label_logo.grid(row=0, pady=5)

        block1.grid(row=1, pady=5)
        label1.grid(row=0, sticky="w")
        entry1.grid(row=1)

        block2.grid(row=2, pady=5)
        label2.grid(row=0, sticky="w")
        entry2.grid(row=1)

        block3.grid(row=3, pady=10)
        button.grid(row=0)

        resultado.grid(row=4)

        window.mainloop()


# Initiate program
App()
