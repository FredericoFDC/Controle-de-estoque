rolamento = []
valor = []

def loja2():
    escolha = str(input("Digite:\n"
                        "1 para adicionar um novo rolamento. \n"
                        "2 para ver o estoque de peças. \n"
                        "3 para remover um rolamento do estoque. \n"
                        "4 para voltar ao inicio : ")).strip()

    if escolha != "1" and "2" and "3":
        print("Digite 1 ou 2 ou 3 para continuar por favor.")

    if escolha == "1":
        novo_rolamento = str(input("Digite seu novo rolamento: ")).strip()
        valor_rolamento = str(input("Digite o valor da peça: ")).strip()

        if novo_rolamento not in rolamento:
            rolamento.append(novo_rolamento)
            valor.append(valor_rolamento)
        else:
            print('Este rolamento não pode ser adicionado porque já existe no estoque.')

    elif escolha == "2":
        for novo_rolamento, valor_rolamento in zip(rolamento, valor):
            print(f'O plato do {novo_rolamento}, custa R$ {valor_rolamento}')

    elif escolha == "3":
        remover = str(input("Qual plato deseja remover: "))
        if remover in rolamento:
            rolamento.remove(remover)
        elif remover not in rolamento:
            print("Este plato não exist no estoque")
            print(f'Estes são os platores do estoque {rolamento}')
    return
