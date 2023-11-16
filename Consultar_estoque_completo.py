import mysql.connector
from ConeccaoComBanco import criar_conexao

def mostrar_estoque():
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Consulta SQL para obter id, plato, marca, valor e quantidade do estoque
        sql_select = "SELECT id, plato, marca, valor, quantidade FROM plato"

        # Executar a consulta SELECT
        cursor.execute(sql_select)

        # Obter todos os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        if resultados:
            print("Estoque Completo:")
            for linha in resultados:
                id, plato, marca, valor, quantidade = linha
                print(f"ID: {id}, Plato: {plato}, Marca: {marca}, Valor: {valor}, Quantidade: {quantidade}")
        else:
            print("O estoque está vazio.")

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

# Exemplo de uso da função para mostrar o estoque completo
mostrar_estoque()
