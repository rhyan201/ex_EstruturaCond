usuario_correto = str("admin")

usuario = str(input("Digite o seu login: "))

if usuario == usuario_correto:
    print("Acesso concedido!")
else:
    print("Acesso negado!")