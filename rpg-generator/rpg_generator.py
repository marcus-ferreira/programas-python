# Gerador de aventuras RPG

import pandas as pd
import random

while True:
    df = pd.read_csv("rpg_generator_db.csv")
    goal = df["Objetivo"][random.randint(0, 35)]
    location = df["Local"][random.randint(0, 35)]
    villain = df["Vilão"][random.randint(0, 35)]
    ally = df["Aliado"][random.randint(0, 35)]
    complication = df["Complicação"][random.randint(0, 35)]
    print(f"Objetivo: {goal}\nLocal: {location}\nVilão: {villain}\nAliado(s): {ally}\nComplicação: {complication}\n")
    print("Aperte Enter para gerar outra aventura\nDigite qualquer coisa para finalizar")
    if input() != "":
        break
