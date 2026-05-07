distancia = int(input("Digite a distância que você irá percorrer: "))

if distancia <= 200:
    vfinal = distancia*0.5
    print(f"Será cobrado o valor de 0,50 centavos por quilômetro, pois sua rota é menor que 200km! Valor final: {vfinal}")
elif distancia > 200:
    vfinal = distancia*0.45
    print(f"Será cobrado o valor de 0,45 centavos por quilômetro, pois sua rota é maior que 200km! Valor final: {vfinal}")