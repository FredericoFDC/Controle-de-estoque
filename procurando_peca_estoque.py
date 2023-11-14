import mysql.connector
from ConeccaoComBanco import criar_conexao

def procurar_produto(criterio):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Instrução SQL para procurar um produto pelo nome e obter informações adicionais
        sql_select = "SELECT plato, marca, valor, quantidade FROM plato WHERE plato LIKE %s"

        # Parâmetro para a consulta
        parametro = f"%{criterio}%"

        # Executar a consulta SELECT
        cursor.execute(sql_select, (parametro,))

        # Obter todos os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        if resultados:
            print("Resultados da pesquisa:")
            for linha in resultados:
                print(f"Nome: {linha[0]}, Marca: {linha[1]}, Valor: {linha[2]}, Quantidade: {linha[3]}")
        else:
            print("Nenhum produto encontrado.")

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
while True:
    # Exemplo de uso da função para procurar um produto pelo nome
    nome_produto = input("Digite o nome do produto para buscar: ")
    procurar_produto(nome_produto)
