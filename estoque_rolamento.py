rolamento = []
valor = []
while True:
    escolha = str(input("Digite 1 para adicionar um novo rolamento e 2 para ver o estoque de peças: ")).strip()

    if escolha != "1" and "2":
        print("Digite 1 ou 2 para continuar por favor.")

    if escolha == "1":
        novo_rolamento = str(input("Digite seu novo rolamento: ")).strip()
        valor_rolamento = str(input("Digite o valor da peça: ")).strip()

        if novo_rolamento not in rolamento:
            rolamento.append(novo_rolamento)
            valor.append(valor_rolamento)
        else:
            print('Este produto já foi adicionada.')

    elif escolha == "2":
        for novo_rolamento, valor_rolamento in zip(rolamento, valor):
            print(f'O rolamento do {novo_rolamento}, custa R$ {valor_rolamento}')

