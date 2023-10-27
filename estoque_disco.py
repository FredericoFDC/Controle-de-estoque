disco = []
valor = []
while True:
    escolha = str(input("Digite 1 para adicionar um novo disco e 2 para ver o estoque de peças, digite 3 para sair: ")).strip()

    if escolha != "1" and "2" and "3":
        print("Digite 1 ou 2 ou 3 para continuar por favor.")

    if escolha == "1":
        novo_disco = str(input("Digite seu novo disco: ")).strip()
        valor_disco = str(input("Digite o valor da peça: ")).strip()

        if novo_disco not in disco:
            disco.append(novo_disco)
            valor.append(valor_disco)
        else:
            print('Este produto já foi adicionada.')

    elif escolha == "2":
        for novo_disco, valor_disco in zip(disco, valor):
            print(f'O disco do {novo_disco}, custa R$ {valor_disco}')

    else:
        break
        