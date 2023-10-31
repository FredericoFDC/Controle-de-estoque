
print('Seja bem vindo ao controle de estoque')

while True:

    estoque = str(input("Oque deseja fazer :\n"
                        "Estoque de plato: 1\n"
                        "Estoque de disco: 2\n"
                        "Estoque de rolamento: 3\n"
                        "Digite sair para sair.\n"
                        "Digite o numero da sua escolhar: "))

    if estoque == "1":
        from estoque_plato import loja
        print("Você vai ser encaminhado para o estoque de plato.")
        loja()

    elif estoque == "2":
        from estoque_disco import loja1
        print("Você vai ser encaminhado para o estoque de Disco.")
        loja1()

    elif estoque == "3":
        from estoque_rolamento import loja2
        print("Você vai ser encaminhado para o estoque de Rolamento.")
        loja2()
    elif estoque == "sair":
        print('Obrigado pela participação')
        break
    else:
        print("Você nao digitou nem uma das alternativas")
        break
