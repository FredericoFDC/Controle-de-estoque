kits = {
    "axor": {"plato": 700, "disco": 590, "rolamento": 450}
}

while True:
    escolha = input("Digite 1 para entrar na loja:\n"
                    "Digite 2 para adicionar um novo kit na loja:\n"
                    "Para sair digite sair"
                    "Faça sua escolha: ")
    if escolha == "1":
        soma = input("Digite o nome do kit que você quer comprar: ")
        if soma in kits:
            valor1 = kits[soma]["plato"]
            valor2 = kits[soma]["disco"]
            valor3 = kits[soma]["rolamento"]
            resultado = valor1 + valor2 + valor3
            print(f"O valor total do kit {soma} é: R${resultado}")
        else:
            print("Kit não encontrado.")
    elif escolha == "2":
        print("Vamos adicionar um novo kit")
        nome = input("Digite o nome do kit de embreagem:")
        plato = int(input("Digite o valor do plato"))
        disco = int(input("Digite o valor do disco"))
        rolamento = int(input("Digite o valor do rolamento"))

        novo_valor = {nome: {"plato": plato, "disco": disco, "rolamento": rolamento}}
        kits.update(novo_valor)
        print(f"Kit '{nome}' adicionado com sucesso.")

    elif escolha == "sair":
        print("Obrigado pela participação")
        break