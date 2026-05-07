l1 = float(input("Digite o tamanho do primeiro lado (em cm): "))
l2 = float(input("Digite o tamanho do segundo lado (em cm): "))
l3 = float(input("Digite o tamanho do terceiro lado (em cm): "))

if l1 == l2 == l3:
    print("É um triângulo equilátero!")
elif l1==l2 and l1 != l3 or l1 == l3 and l1!=l2 or l2 ==l3 and l2 !=l1:
    print("É um triângulo isósceles!")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("É um triângulo escaleno")
