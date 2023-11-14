import mysql.connector
from ConeccaoComBanco import criar_conexao
while True:
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Obter dados do usuário
        #idnovo = input("Digite o numero do id: ")
        platonovo = input("Digite o nome do plato novo: ")
        marcanova = input("Digite a marca do plato novo: ")
        valornovo = input("Digite o valor do plato novo: ")
        quantidadenova = input("Digite quantos platores novo estã sendo adicionados: ")

        # Instrução SQL para realizar o INSERT
        sql_insert = "INSERT INTO plato (plato, marca, valor, quantidade) VALUES (%s, %s, %s, %s)"

        # Dados a serem inseridos
        dados = (platonovo, marcanova, valornovo, quantidadenova)

        # Executar a consulta de inserção
        cursor.execute(sql_insert, dados)

        # Commit das mudanças
        conexao.commit()

        # Exemplo de consulta SELECT
        query = "SELECT * FROM plato"
        cursor.execute(query)

        # Obter todos os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        for linha in resultados:
            print(linha)

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
