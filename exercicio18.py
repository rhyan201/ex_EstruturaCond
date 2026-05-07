valorcasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor de seu salário: "))
anospgt = int(input("Digite em quantos anos você pretende pagar: "))

prestmensal = (valorcasa/anospgt)/12

if prestmensal< salario*0.3:
    print("Empréstimo aprovado.")

elif prestmensal > salario*0.3:
    print("Empréstimo negado.")