
print('Seja bem vindo ao controle de estoque')

while True:
    contador = 0
    estoque = int(input("Oque deseja fazer :\n"
                        "Estoque de plato: 1\n"
                        "Estoque de disco: 2\n"
                        "Estoque de rolamento: 3\n"
                        "Digite o numero da sua escolhar: "))

    valor = contador + estoque

    if valor == 1:
        import estoque_plato
        print("Você vai ser encaminhado para o estoque de plato.")
        print(estoque_plato)

    elif valor == 2:
        import estoque_disco
        print("Você vai ser encaminhado para o estoque de Disco.")
        print(estoque_disco)

    elif valor == 3:
        import estoque_rolamento
        print("Você vai ser encaminhado para o estoque de Rolamento.")
        print(estoque_rolamento)
    else:
        print("Você nao digitou nem uma das alternativas")
        break

