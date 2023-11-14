import mysql.connector
from ConeccaoComBanco import criar_conexao


def remover_quantidade(nome_peca, quantidade):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Verificar a quantidade atual da peça no estoque
        sql_select = "SELECT quantidade FROM plato WHERE plato = %s"
        cursor.execute(sql_select, (nome_peca,))
        resultado = cursor.fetchone()

        if resultado:
            quantidade_atual = resultado[0]

            # Verificar se a quantidade a ser removida não excede a quantidade atual
            if quantidade <= quantidade_atual:
                # Consumir todos os resultados antes de prosseguir
                cursor.fetchall()

                # Atualizar a quantidade no estoque
                nova_quantidade = quantidade_atual - quantidade
                sql_update = "UPDATE plato SET quantidade = %s WHERE plato = %s"
                cursor.execute(sql_update, (nova_quantidade, nome_peca))

                # Commit da transação
                conexao.commit()

                print(f"Foram removidas {quantidade} unidades da peça '{nome_peca}' do estoque.")

                # Exibir a quantidade restante
                print(f"Quantidade restante da peça '{nome_peca}': {nova_quantidade}")

            else:
                print("Erro: A quantidade a ser removida é maior do que a quantidade atual no estoque.")
        else:
            print("Erro: Peça não encontrada no estoque.")

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()


while True:
    # Exemplo de uso da função para remover uma quantidade de uma peça
    nome_peca_remover = input("Digite o nome da peça: ")
    quantidade_remover = int(input("Digite a quantidade a ser removida: "))
    remover_quantidade(nome_peca_remover, quantidade_remover)
