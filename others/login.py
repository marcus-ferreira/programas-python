import tkinter as tk
import pyodbc
import pandas as pd
from tkinter import ttk

class App:
    def __init__(self):
        # Functions
        def signup():
            if ent_username.get() != "" and ent_password.get() != "":
                query = f"SELECT * FROM [dbo].[Users] WHERE Username = '{ent_username.get()}'"
                df = pd.read_sql(query, conn)
                if not df["Username"].any():
                    cursor.execute(f'''INSERT INTO testDB.dbo.Users(Username, Password) VALUES ('{ent_username.get()}', '{ent_password.get()}')''')
                    conn.commit()
                    lbl_info.config(text="Usuário cadastrado!")
                else:
                    lbl_info.config(text="Usuário já existe no sistema!")
            else:
                lbl_info.config(text="Insira as informações corretas!")
            ent_username.delete(0, "end")
            ent_password.delete(0, "end")

        def login():
            if ent_username.get() != "" and ent_password.get() != "":
                query = f"SELECT * FROM [dbo].[Users] WHERE Username = '{ent_username.get()}' AND Password = '{ent_password.get()}'"
                df = pd.read_sql(query, conn)
                if df["Username"][0] == ent_username.get() and df["Password"][0] == ent_password.get():
                    lbl_info.config(text="Login executado!")
                    ent_username.delete(0, "end")
                    ent_password.delete(0, "end")
                else:
                    lbl_info.config(text="Senha incorreta!")
            else:
                lbl_info.config(text="Insira as informações corretas!")


        # Database
        conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=<server_name>; DATABASE=<database_name>; Trusted_Connection=yes;')
        cursor = conn.cursor()


        # GUI
        window = tk.Tk()
        window.title("Sign up / Log in Example")

        lbl_title = tk.Label(window, text="Login", font="Verdana 16 bold")
        lbl_username = tk.Label(window, text="Usuário:")
        ent_username = tk.Entry(window)
        lbl_password = tk.Label(window, text="Senha:")
        ent_password = tk.Entry(window, show="*")
        btn_signup = tk.Button(window, text="signup", command=signup)
        btn_login = tk.Button(window, text="Entrar", command=login)
        lbl_info = tk.Label(window, text="")


        # Grid
        lbl_title.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        lbl_username.grid(row=1, column=0, sticky="w")
        ent_username.grid(row=1, column=1, padx=2, pady=2)
        lbl_password.grid(row=2, column=0, sticky="w")
        ent_password.grid(row=2, column=1, padx=2, pady=2)
        btn_signup.grid(row=3, column=0, sticky="we", columnspan=2, padx=2, pady=2)
        btn_login.grid(row=4, column=0, sticky="we", columnspan=2, padx=2, pady=2)
        lbl_info.grid(row=5, column=0, columnspan=2)


        window.mainloop()


App()
