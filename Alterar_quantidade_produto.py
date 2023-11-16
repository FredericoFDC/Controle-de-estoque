import mysql.connector
from ConeccaoComBanco import criar_conexao

def alterar_quantidade(nome_peca, nova_quantidade):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Consulta SQL para obter a quantidade atual
        sql_select = "SELECT quantidade FROM plato WHERE plato = %s"
        cursor.execute(sql_select, (nome_peca,))
        resultado = cursor.fetchone()

        if resultado:
            quantidade_atual = resultado[0]

            # Exibir a quantidade atual
            print(f"Quantidade Atual da Peça '{nome_peca}': {quantidade_atual}")

            # Atualizar a quantidade no estoque
            nova_quantidade_total = quantidade_atual + nova_quantidade
            sql_update = "UPDATE plato SET quantidade = %s WHERE plato = %s"
            cursor.execute(sql_update, (nova_quantidade_total, nome_peca))

            # Commit da transação
            conexao.commit()

            print(f"Foram adicionadas {nova_quantidade} unidades à peça '{nome_peca}'.")
            print(f"Nova Quantidade Total: {nova_quantidade_total}")

        else:
            print("Erro: Peça não encontrada no estoque.")

        # Consumir os resultados antes de fechar o cursor
        cursor.fetchall()

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

while True:
    # Exemplo de uso da função para alterar a quantidade de uma peça
    nome_peca_alterar = input("Digite o nome da peça para alterar a quantidade: ")
    quantidade_alterar = int(input("Digite a quantidade a ser adicionada: "))
    alterar_quantidade(nome_peca_alterar, quantidade_alterar)
