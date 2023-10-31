def estoque(novo_plato, plato, valor_plato, valor):
    if novo_plato not in plato:
        plato.append(novo_plato)
        valor.append(valor_plato)

plato = []
valor = []
def loja():

    escolha = str(input("Digite:\n"
                        "1 para adicionar um novo plato. \n"
                        "2 para ver o estoque de peças. \n"
                        "3 para remover um plato do estoque. \n"
                        "4 para voltar ao inicio : ")).strip()

    if escolha != "1" and "2" and "3":
        print("Digite 1 ou 2 ou 3 para continuar por favor.")


    if escolha == "1":
        novo_plato = str(input("Digite seu novo plato: ")).strip()
        valor_plato = str(input("Digite o valor da peça: ")).strip()

        estoque(novo_plato, plato, valor_plato, valor)
        #if novo_plato not in plato:
            #plato.append(novo_plato)
            #valor.append(valor_plato)
        #else:
            #print('Este plato não pode ser adicionado por que já existe no estoque.')

    elif escolha == "2":
        for novo_plato, valor_plato in zip(plato, valor):
            print(f'O plato do {novo_plato}, custa R$ {valor_plato}')

    elif escolha == "3":
        remover = str(input("Qual plato deseja remover: "))
        if remover in plato:
            plato.remove(remover)
        elif remover not in plato:
            print("Este plato não exist no estoque")
            print(f'Estes são os platores do estoque {plato}')
    return
