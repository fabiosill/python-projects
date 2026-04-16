try:
    usuario = input("Usuario: ")
    senha = input("Senha: ")

    if not usuario or not senha:
        raise ValueError("Campos nao podem ficar vazios")

    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso!")
    else:
        print("Usuario ou senha incorretos.")

except ValueError as erro:
    print("Erro:", erro)

except Exception as e:
    print("Ocorreu um erro inesperado:", e)