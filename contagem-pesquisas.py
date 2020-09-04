# Contagem de Pesquisas #

# Definição da função do programa
def program():

    # Definição das varíaveis
    q1 = {"Muito bom": 0, "Bom": 0, "Regular": 0, "Ruim": 0}
    q2 = {"Muito bom": 0, "Bom": 0, "Regular": 0, "Ruim": 0}
    q3 = {"Sim": 0, "Não": 0}

    while True:
        # Pergunta 1
        print("Como você classifica o atendimento médico da clínica?")
        print("(1) Muito bom, (2) Bom, (3) Regular, (4) Ruim, (Enter) Finalizar")
        q1r = input()
        print()
        if q1r == "1":
            q1["Muito bom"] += 1
        elif q1r == "2":
            q1["Bom"] += 1
        elif q1r == "3":
            q1["Regular"] += 1
        elif q1r == "4":
            q1["Ruim"] += 1
        else:
            break

        # Pergunta 2
        print("Como você classifica as instalações da clínica com relação ao espaço físico e conforto?")
        print("(1) Muito bom, (2) Bom, (3) Regular, (4) Ruim, (Enter) Finalizar")
        q2r = input()
        print()
        if q2r == "1":
            q2["Muito bom"] += 1
        elif q2r == "2":
            q2["Bom"] += 1
        elif q2r == "3":
            q2["Regular"] += 1
        elif q2r == "4":
            q2["Ruim"] += 1
        else:
            break

        # Pergunta 3
        print("Você recomendaria a clínica para colegas de trabalho outras empresas?")
        print("(1) Sim, (2) Não, (Enter) Finalizar")
        q3r = input();
        print()
        if q3r == "1":
            q3["Sim"] += 1
        elif q3r == "2":
            q3["Não"] += 1
        else:
            break

    # Imprime os resultados
    print("Atendimento médico")
    print(q1)
    print("\nInstalações da clínica")
    print(q2)
    print("\nRecomendação")
    print(q3)
    print()

    # Reinicia
    restart = input("Reiniciar? (s/n)\n")
    if restart == "s":
        program()

# Inicia o programa
program()
