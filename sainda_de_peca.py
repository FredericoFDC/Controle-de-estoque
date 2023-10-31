plato = ["axor", "mercedes", "vw"]
valor = [120, 150, 200]

#print(plato)
#plato.remove("axor")
#print(plato)
def remover_peca():
    saida = str(input("Digite o nome do produto que deseja remover ou digite 2 para voltar a pagina inicial: "))

    if saida not in plato:
        print("Esse plato não exite no estoque")
    elif saida in plato:
        plato.remove(saida)
        print(plato)
    elif saida == "2":
        return 
    else:
        print("Algo esta errado")
        return


