import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        def calcular():
            try: 
                sexo = combobox_sexo.get()
                idade = int(entry_idade.get())
                peso = float(entry_peso.get().replace(",", "."))
                altura = float(entry_altura.get().replace(",", "."))
                naf = combobox_naf.get()

                # IMC
                if 20 <= idade < 59:
                    imc = round(peso / (altura ** 2), 2)
                else:
                    imc = None

                # IMC médio
                if sexo == "Masculino":
                    imc_medio = 22
                elif sexo == "Feminino":
                    imc_medio = 20

                # IMC Título
                if imc == 0:
                    imc_titulo = "Não calculado devido à faixa etária"
                elif 0 < imc < 16:
                    imc_titulo = "Magreza Grau III"
                elif 16.0 <= imc < 17:
                    imc_titulo = "Magreza Grau II"
                elif 17.0 <= imc < 18.5:
                    imc_titulo = "Magreza Grau I"
                elif 18.5 <= imc < 25:
                    imc_titulo = "Eutrofia"
                elif 25.0 <= imc < 30:
                    imc_titulo = "Sobrepeso"
                elif 30.0 <= imc < 35:
                    imc_titulo = "Obesidade Grau I"
                elif 35.0 <= imc < 40:
                    imc_titulo = "Obesidade Grau II"
                elif imc >= 40.0:
                    imc_titulo = "Obesidade Grau III"

                # Peso teórico
                peso_teorico = round(imc_medio * (altura ** 2), 2)

                # TMB
                if sexo == "Masculino":
                    if idade < 3:
                        tmb = round(59.512 * peso - 30.4)
                    elif 3 <= idade < 10:
                        tmb = round(22.706 * peso + 504.3)
                    elif 10 <= idade < 18:
                        tmb = round(17.686 * peso + 658.2)
                    elif 18 <= idade < 30:
                        tmb = round(15.057 * peso + 692.2)
                    elif 30 <= idade < 60:
                        tmb = round(11.472 * peso + 873.1)
                    elif idade >= 60:
                        tmb = round(11.711 * peso + 587.7)
                elif sexo == "Feminino":
                    if idade < 3:
                        tmb = round(58.317 * peso - 31.1)
                    elif 3 <= idade < 10:
                        tmb = round(20.317 * peso + 485.9)
                    elif 10 <= idade < 18:
                        tmb = round(13.384 * peso + 692.6)
                    elif 18 <= idade < 30:
                        tmb = round(14.818 * peso + 486.6)
                    elif 30 <= idade < 60:
                        tmb = round(8.126 * peso + 845.6)
                    elif idade >= 60:
                        tmb = round(9.082 * peso + 658.5)

                # VET
                if naf == "Sedentário" or naf == "Moderado":
                    vet = round(tmb * 1.53)
                elif naf == "Ativo":
                    vet = round(tmb * 1.76)
                elif naf== "Muito Ativo":
                    vet = round(tmb * 2.25)

                # GTE
                if 9 <= idade < 18:
                    if sexo == "Masculino":
                        if naf == "Sedentário":
                            gte = round(88.5 - 61.9 * idade + 1.0 * (26.7 * peso + 903 * altura) + 25)
                        elif naf == "Moderado":
                            gte = round(88.5 - 61.9 * idade + 1.13 * (26.7 * peso + 903 * altura) + 25)
                        elif naf == "Ativo":
                            gte = round(88.5 - 61.9 * idade + 1.26 * (26.7 * peso + 903 * altura) + 25)
                        elif naf == "Muito Ativo":
                            gte = round(88.5 - 61.9 * idade + 1.42 * (26.7 * peso + 903 * altura) + 25)
                    elif sexo == "Feminino":
                        if naf == "Sedentário":
                            gte = round(135.3 - 30.8 * idade + 1.0 * (10 * peso + 934 * altura) + 20)
                        elif naf == "Moderado":
                            gte = round(135.3 - 30.8 * idade + 1.16 * (10 * peso + 934 * altura) + 20)
                        elif naf == "Ativo":
                            gte = round(135.3 - 30.8 * idade + 1.31 * (10 * peso + 934 * altura) + 20)
                        elif naf == "Muito Ativo":
                            gte = round(135.3 - 30.8 * idade + 1.56 * (10 * peso + 934 * altura) + 20)
                elif idade >= 18:
                    if sexo == "Masculino":
                        if naf == "Sedentário":
                            gte = round(662 - 9.53 * idade + 1.0 * (15.91 * peso + 539.6 * altura))
                        elif naf == "Moderado":
                            gte = round(662 - 9.53 * idade + 1.11 * (15.91 * peso + 539.6 * altura))
                        elif naf == "Ativo":
                            gte = round(662 - 9.53 * idade + 1.25 * (15.91 * peso + 539.6 * altura))
                        elif naf == "Muito Ativo":
                            gte = round(662 - 9.53 * idade + 1.48 * (15.91 * peso + 539.6 * altura))
                    elif sexo == "Feminino":
                        if naf == "Sedentário":
                            gte = round(354 - 6.91 * idade + 1.0 * (9.35 * peso + 726 * altura))
                        elif naf == "Moderado":
                            gte = round(354 - 6.91 * idade + 1.12 * (9.35 * peso + 726 * altura))
                        elif naf == "Ativo":
                            gte = round(354 - 6.91 * idade + 1.27 * (9.35 * peso + 726 * altura))
                        elif naf == "Muito Ativo":
                            gte = round(354 - 6.91 * idade + 1.45 * (9.35 * peso + 726 * altura))

                label_resultado.config(text= f"IMC: {imc} - {imc_titulo}\nPeso Teórico: {peso_teorico} kg\nTMB: {tmb}\nVET: {vet}\nGTE: {gte}")
            except:
                label_resultado.config(text= "Insira os valores corretamente!")

        # Apagar
        def apagar():
            combobox_sexo.set("")
            entry_idade.delete(0, "end")
            entry_peso.delete(0, "end")
            entry_altura.delete(0, "end")
            combobox_naf.set("")
            label_resultado.config(text= "")

        # GUI
        window = tk.Tk()
        window.title("Avaliação Nutricional")
        window.resizable(False, False)
        window.iconbitmap("nutrition.ico")

        # LabelFrame 1
        lblfrm_dados = tk.LabelFrame(window, text="Dados")

        frame_dados = tk.Frame(lblfrm_dados)
        label_sexo = tk.Label(frame_dados, text="Sexo:")
        combobox_sexo = ttk.Combobox(frame_dados, values=["Masculino", "Feminino"], state="readonly", width=15)
        label_idade = tk.Label(frame_dados, text="Idade:")
        entry_idade = tk.Entry(frame_dados, width=15)
        label_peso = tk.Label(frame_dados, text="Peso:")
        entry_peso = tk.Entry(frame_dados, width=15)
        label_altura = tk.Label(frame_dados, text="Altura:")
        entry_altura = tk.Entry(frame_dados, width=15)
        label_naf = tk.Label(frame_dados, text="Atividade Física:")
        combobox_naf = ttk.Combobox(frame_dados, values=["Sedentário", "Moderado", "Ativo", "Muito Ativo"], state="readonly", width=15)

        frame_botoes = tk.Frame(lblfrm_dados)
        button_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular)
        button_apagar = tk.Button(frame_botoes, text="Apagar", command=apagar)

        # LabelFrame 2
        lblfrm_resultado = tk.LabelFrame(window, text="Resultado")
        label_resultado = tk.Label(lblfrm_resultado, width=40, height=10)

        # Grid
        lblfrm_dados.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=5)
        frame_dados.grid(row=0, column=0)
        label_sexo.grid(row=0, column=0, sticky="w", pady=1)
        combobox_sexo.grid(row=0, column=1, sticky="we", pady=1)
        label_idade.grid(row=1, column=0, sticky="w", pady=1)
        entry_idade.grid(row=1, column=1, sticky="we", pady=1)
        label_peso.grid(row=2, column=0, sticky="w", pady=1)
        entry_peso.grid(row=2, column=1, sticky="we", pady=1)
        label_altura.grid(row=3, column=0, sticky="w", pady=1)
        entry_altura.grid(row=3, column=1, sticky="we", pady=1)
        label_naf.grid(row=4, column=0, sticky="w", pady=1)
        combobox_naf.grid(row=4, column=1, sticky="we", pady=1)

        frame_botoes.grid(row=1, column=0, pady=5)
        button_calcular.grid(row=0, column=0, sticky="e", padx=5)
        button_apagar.grid(row=0, column=1, sticky="e", padx=5)

        lblfrm_resultado.grid(row=0, column=1, padx=10, pady=5, ipadx=5, ipady=5)
        label_resultado.grid(row=0, column=0)

        # Main loop
        window.mainloop()

App()
