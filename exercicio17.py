mquad = float(input("Digite o tamanho (em m²) a ser pintado: "))

lata = mquad/3

if lata <= 18:
    print("Você deve comprar apenas uma lata de tinta! O valor de cada lata de tinta é de R$80,00")
elif lata > 18:
    print("Você deve comprar mais de uma lata de tinta! O valor de cada lata de tinta é de R$80,00")