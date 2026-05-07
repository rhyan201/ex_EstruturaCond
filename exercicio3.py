preco = float(input("Digite o valor da compra: "))

if preco > 100.00:
    valordesconto = preco*10/100
    valorfinal = preco-valordesconto
    print("O valor da compra com o desconto é: R$", valorfinal)
elif preco <= 100.00:
    print("Nas compras acima de 100, você ganha 10% de desconto!")