import mysql.connector
from ConeccaoComBanco import criar_conexao


def adicionar_quantidade(nome_peca, quantidade):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Verificar se a peça já existe no estoque
        sql_select = "SELECT quantidade FROM plato WHERE plato = %s"
        cursor.execute(sql_select, (nome_peca,))
        resultado = cursor.fetchone()

        if resultado:
            quantidade_atual = resultado[0]

            # Consumir todos os resultados antes de prosseguir
            cursor.fetchall()

            # Calcular a nova quantidade
            nova_quantidade = quantidade_atual + quantidade

            # Atualizar a quantidade no estoque
            sql_update = "UPDATE plato SET quantidade = %s WHERE plato = %s"
            cursor.execute(sql_update, (nova_quantidade, nome_peca))

            # Commit da transação
            conexao.commit()

            print(f"Foram adicionadas {quantidade} unidades da peça '{nome_peca}' ao estoque.")

            # Exibir a nova quantidade
            print(f"Nova quantidade da peça '{nome_peca}': {nova_quantidade}")

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


# Exemplo de uso da função para adicionar uma quantidade a uma peça
while True:
    nome_peca_adicionar = input("Digite o nome da peça: ")
    quantidade_adicionar = int(input("Digite a quantidade a ser adicionada: "))
    adicionar_quantidade(nome_peca_adicionar, quantidade_adicionar)
