salario = float(input("Digite o seu salário: "))

if salario > 1621:
    aumento = (salario*0.10)+salario
    print(f"O seu salário atual é de: {salario}. Com o aumento de 10% passará a ser:{aumento}")
elif salario <=1621:
    aumento = (salario*0.15)+salario
    print(f"O seu salário atual é de: {salario}. Com o aumento de 15% passará a ser: {aumento}")