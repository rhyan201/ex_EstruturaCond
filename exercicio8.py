peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso/(altura**2)

if imc>25:
    print("Acima do peso ideal")
else:
    print("Peso dentro da normalidade")