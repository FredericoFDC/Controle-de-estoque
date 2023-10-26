
plato = []
valor = []
while True:
    escolha = int(input("Digite 1 para adicionar um novo plato e 2 para ver o estoque de peças: "))

    if escolha == 1:
        novo_plato = str(input("Digite seu novo plato: ")).strip()
        valor_plato = str(input("Digite o valor da peça: "))

        if novo_plato not in plato:
            plato.append(novo_plato)
            valor.append(valor_plato)
        else:
            print('Já foi adicionada.')

    elif escolha == 2:
        for novo_plato, valor_plato in zip(plato, valor):

            marca = novo_plato.replace("'", " ")
            valor = valor_plato.replace("'", " ")

            print(f'O plato do {marca} custa R$ {valor}.')

