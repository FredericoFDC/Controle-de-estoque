def estoque(novo_plato, plato, valor):
    if novo_plato not in plato:
        plato.append(novo_plato)
        valor.append(valor_plato)

plato = []  # Inicialize a lista de pratos
valor = []

while True:
    novo_plato = input("Digite um plato (ou digite 'sair' para encerrar): ")
    if novo_plato.lower() == "sair":
        break
    valor_plato = str(input((f'Digite um novo valor para plato do {novo_plato}: ')))

    estoque(novo_plato, plato, valor)

for n in zip(plato, valor):
    print(n)
 