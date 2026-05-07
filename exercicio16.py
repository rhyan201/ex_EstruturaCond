tempC = float(input("Digite a temperatura (em C°): "))

convers = str(input("Você quer converter para Fahrenheit (F) ou Kelvin (K)? Digite F ou K: "))

if  convers == str("K"):
    kelvin = tempC + 237.15
    print(f"A temperatura em C° {tempC} convertida para Kelvin é de {kelvin}K")
elif convers == str("F"):
    fahre = (tempC*1.8)+32
    print(f"A temperatura em C° {tempC} convertida para Fahrenheit é de {fahre}F")