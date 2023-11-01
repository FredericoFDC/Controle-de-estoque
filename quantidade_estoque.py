plato = ["axor","axor","axor","axor","axor","axor","mercedes","new"]

while True:
    pesquisa = str(input("Digite 1 para saber o tamanho do estoque do plato.\n"
                        "Digite 2 para saber a quantidade de plato especifico.\n"
                        "Para deixar o controle de estoque digite sair\n"
                        "Digite sua escolha: "))

    if pesquisa == "1":
        print(len(plato))
        print(plato)

    elif pesquisa == "2":
        busca = str(input("Digite o nome do plato para pesquisa: "))

        if busca in plato:
            print(plato.count(busca))

        elif busca not in plato:
            print("Plato não encontrado no estoque")

    elif pesquisa == "sair":
        print("Obrigado por colaborar")
        break

    else:
        print("Você digitiou algo não esperado")
