import mysql.connector
from ConeccaoComBanco import criar_conexao

def pesquisar_peca(nome_peca):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Instrução SQL para pesquisar uma peça pelo nome
        sql_select = "SELECT * FROM plato WHERE plato = %s"

        # Executar a consulta SELECT
        cursor.execute(sql_select, (nome_peca,))

        # Obter todos os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        if resultados:
            print("Informações da peça:")
            for linha in resultados:
                print("ID:", linha[0])
                print("Nome da Peça:", linha[1])
                print("Marca:", linha[2])
                print("Valor:", linha[3])
                # Adicione mais campos conforme necessário

        else:
            print("Nenhuma peça encontrada no estoque com o nome fornecido.")

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

while True:
    # Exemplo de uso da função para pesquisar uma peça pelo nome
    nome_peca_pesquisar = input("Digite o nome da peça para pesquisar: ")
    pesquisar_peca(nome_peca_pesquisar)
