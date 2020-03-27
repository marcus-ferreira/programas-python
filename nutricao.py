# Dados
sexo = input("Qual o seu sexo? (m/f) ")
idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
af = int(input("Qual seu nível de atividade física?\n(1) Sedentário/leve\n"
           "(2) Ativo/moderadamente ativo\n(3) Vigoroso/moderadamente vigoroso "))
ocupacao = input("Qual a sua ocupação? ")
print()

# IMC
imc = peso / (altura ** 2)
if imc < 16.0:
    print(f"IMC: {imc:.1f} (Magreza Grau III)")
elif 16.0 <= imc < 16.9:
    print(f"IMC: {imc:.1f} (Magreza Grau II)")
elif 17.0 <= imc < 18.4:
    print(f"IMC: {imc:.1f} (Magreza Grau I)")
elif 18.5 <= imc < 24.9:
    print(f"IMC: {imc:.1f} (Eutrofia)")
elif 25.0 <= imc < 29.9:
    print(f"IMC: {imc:.1f} (Sobrepeso)")
elif 30.0 <= imc < 34.9:
    print(f"IMC: {imc:.1f} (Obesidade Grau I)")
elif 35.0 <= imc < 39.9:
    print(f"IMC: {imc:.1f} (Obesidade Grau II)")
elif imc >= 40.0:
    print(f"IMC: {imc:.1f} (Obesidade Grau III)")

# Peso Teórico
if sexo == "m":
    imc_medio = 22
else:
    imc_medio = 20.8
peso_teorico = imc_medio * (altura ** 2)
print(f"Peso Teórico: {peso_teorico:.1f} Kg")

# TMB
if sexo == "m":
    if idade < 3:
        tmb = 59.512 * peso - 30.4
    elif 3 <= idade < 10:
        tmb = 22.706 * peso + 504.3
    elif 10 <= idade < 18:
        tmb = 17.686 * peso + 658.2
    elif 18 <= idade < 30:
        tmb = 15.057 * peso + 692.2
    elif 30 <= idade < 60:
        tmb = 11.472 * peso + 873.1
    elif idade >= 60:
        tmb = 11.711 * peso + 587.7
else:
    if idade < 3:
        tmb = 58.317 * peso - 31.1
    elif 3 <= idade < 10:
        tmb = 20.317 * peso + 485.9
    elif 10 <= idade < 18:
        tmb = 13.384 * peso + 692.6
    elif 18 <= idade < 30:
        tmb = 14.818 * peso + 486.6
    elif 30 <= idade < 60:
        tmb = 8.126 * peso + 845.6
    elif idade >= 60:
        tmb = 9.082 * peso + 658.5
print(f"TMB: {tmb:.0f} Kcal/dia")

# VET
if af == 1:
    vet = tmb * 1.53
elif af == 2:
    vet = tmb * 1.76
else:
    vet = tmb * 2.25
print(f"VET: {vet:.3f} Kcal/dia")
