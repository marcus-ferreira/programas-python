import tkinter as tk
import pyodbc
import pandas as pd
from tkinter import ttk

class App:
    def __init__(self):
        # Functions
        def cadastrar():
            if entry1.get() != "" and entry2.get() != "":
                cursor.execute(f'''
                    IF NOT EXISTS 
                        (SELECT * FROM [dbo].[Users] 
                        WHERE Username = '{entry1.get()}') 
                            INSERT INTO testDB.dbo.Users(Username, Password) 
                            VALUES ('{entry1.get()}', '{entry2.get()}')
                ''')
                conn.commit()
                label4.config(text="Usuário cadastrado!")
            else:
                label4.config(text="Insira as informações corretas!")
            entry1.delete(0, "end")
            entry2.delete(0, "end")

        def logar():
            if entry1.get() != "" and entry2.get() != "":
                query = f"SELECT * FROM [dbo].[Users] WHERE Username = '{entry1.get()}' AND Password = '{entry2.get()}'"
                df = pd.read_sql(query, conn)
                if df["Username"][0] == entry1.get() and df["Password"][0] == entry2.get():
                    label4.config(text="Login executado!")
                    entry1.delete(0, "end")
                    entry2.delete(0, "end")
                else:
                    label4.config(text="Senha incorreta!")
            else:
                label4.config(text="Insira as informações corretas!")


        # Database
        conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=<server_name>; DATABASE=<database_name>; Trusted_Connection=yes;')
        cursor = conn.cursor()


        # GUI
        window = tk.Tk()
        window.title("Login")

        label1 = tk.Label(window, text="Login", font="Verdana 16 bold")
        label2 = tk.Label(window, text="Usuário:")
        entry1 = tk.Entry(window)
        label3 = tk.Label(window, text="Senha:")
        entry2 = tk.Entry(window, show="*")
        button1 = tk.Button(window, text="Cadastrar", command=cadastrar)
        button2 = tk.Button(window, text="Entrar", command=logar)
        label4 = tk.Label(window, text="")


        # Grid
        label1.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        label2.grid(row=1, column=0, sticky="w")
        entry1.grid(row=1, column=1, padx=2, pady=2)
        label3.grid(row=2, column=0, sticky="w")
        entry2.grid(row=2, column=1, padx=2, pady=2)
        button1.grid(row=3, column=0, sticky="we", columnspan=2, padx=2, pady=2)
        button2.grid(row=4, column=0, sticky="we", columnspan=2, padx=2, pady=2)
        label4.grid(row=5, column=0, columnspan=2)


        window.mainloop()


App()
