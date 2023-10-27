plato = []
valor = []

def loja():
    escolha = str(input("Digite 1 para adicionar um novo plato e 2 para ver o estoque de peças, 3 para voltar ao inicio : ")).strip()

    if escolha != "1" and "2" and "3":
        print("Digite 1 ou 2 ou 3 para continuar por favor.")

    if escolha == "1":
        novo_plato = str(input("Digite seu novo plato: ")).strip()
        valor_plato = str(input("Digite o valor da peça: ")).strip()

        if novo_plato not in plato:
            plato.append(novo_plato)
            valor.append(valor_plato)
        else:
            print('Este produto já foi adicionada.')

    elif escolha == "2":
        for novo_plato, valor_plato in zip(plato, valor):
            print(f'O plato do {novo_plato}, custa R$ {valor_plato}')

    return