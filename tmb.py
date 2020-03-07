# Taxa metabólica

tmb = 0
caloria = 0

print("###########################")
print("## Taxa Metabólica Basal ##")
print("###########################")
print()
print("Qual seu sexo? (m/f)")
sexo = input()
print("Qual seu peso?")
peso = float(input())
print("Qual sua altura?")
altura = float(input())
print("Qual sua idade?")
idade = int(input())
print("Qual seu nível de atividade? (1) Sedentário, (2) Moderavelmente ativo, (3) Muito ativo, (4) Extremamente ativo")
atividade = input()

if sexo == "m":
    tmb = (66.5 + (14 * peso) + (5 * altura) - (6.7 * idade))
else:
    tmb = (655.1 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade))

if atividade == "1":
    caloria = tmb * 1.2
elif atividade == "2":
    caloria = tmb * 1.375
elif atividade == "3":
    caloria = tmb * 1.55
elif atividade == "4":
    caloria = tmb * 1.725
else:
    caloria = tmb * 1.9

print()
print("Seu TMB é %.2f." % tmb)
print("A quantidade de caloria que seu corpo gasta é %.2f kcal." % caloria)
