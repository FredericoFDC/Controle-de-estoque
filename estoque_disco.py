disco = []
valor = []

def loja1():

    escolha = str(input("Digite:\n "
                        "1 para adicionar um novo disco.\n"
                        "2 para ver o estoque de peças.\n"
                        "3 para remover um disco do estoque.\n"
                        "4 para voltar ao inicio : ")).strip()

    if escolha != "1" and "2" and "3":
        print("Digite 1 ou 2 ou 3 para continuar por favor.")

    if escolha == "1":
        novo_disco = str(input("Digite seu novo disco: ")).strip()
        valor_disco = str(input("Digite o valor da peça: ")).strip()

        if novo_disco not in disco:
            disco.append(novo_disco)
            valor.append(valor_disco)
        else:
            print('Este disco não pode ser adicionado por que já existe no estoque.')

    elif escolha == "2":
        for novo_disco, valor_disco in zip(disco, valor):
            print(f'O plato do {novo_disco}, custa R$ {valor_disco}')

    elif escolha == "3":
        remover = str(input("Qual disco deseja remover: "))
        if remover in disco:
            disco.remove(remover)
        elif remover not in disco:
            print("Este plato não exist no estoque")
            print(f'Estes são os platores do estoque {disco}')
    return
