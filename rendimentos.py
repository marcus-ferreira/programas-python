vp = float(input("Qual o valor da aplicação? "))
j = float(input("Qual a taxa de juros? (a.m. em %) ")) / 100
n = int(input("Qual o tempo da aplicação em meses? "))
vf = float(vp * ((1 + j) ** n))
print(f"O valor a ser recebido será de R$ {round(vf, 2)}")
