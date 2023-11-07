kits = {
    "axor": {"plato": 600, "disco": 200, "rolamento": 200}
}

while True:
    escolha = input("Digite 1 para entrar na loja:\n"
                    "Digite 2 para adicionar um novo kit na loja:\n"
                    "Digite 3 para pegar peça com desconto.\n"
                    "Para sair digite sair \n"
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
    elif escolha == "3":
        desconto = str(input("Digite qual kit voce deseja comprar: "))
        porcentagem = int(input("Digite o desconto que vc quer dar % : "))

        if porcentagem > 30:
            print("Você não tem autorização para dar esse desconto")
            continue # Faz o loop voltar ao inicio
        if desconto in kits:
            valor1 = kits[desconto]["plato"]
            valor2 = kits[desconto]["disco"]
            valor3 = kits[desconto]["rolamento"]
            resultado = valor1 + valor2 + valor3
            valores = porcentagem * 0.01
            valores2 = resultado * valores
            valores3 = resultado - valores2
            print(f"O valor total do kit {desconto} é: R${resultado} com desconto ficou R${valores3}")

    elif escolha == "sair":
        print("Obrigado pela participação")
        break