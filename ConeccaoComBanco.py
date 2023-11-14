import mysql.connector

# Conectar ao servidor MySQL local
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estoque"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")
        return None

# Criar um cursor para interagir com o banco de dados
#idnovo = str(input("Digite o numero do id: "))
#platonovo = str(input(("Digite o nome do plato novo: ")))
#marcanova = str(input(("Digite a marca do plato novo: ")))
#valornovo = str(input(("Digite o valor do plato novo: ")))

#cursor = criar_conexao().cursor()
#id = idnovo
#plato = platonovo
#marca = marcanova
#valor = valornovo
#adicionar = "INSERT INTO estoque (id, plato, marca, valor) VALUES (%s, %s, %s, %s)"
#try:
    # Executar a consulta de inserção
    #cursor.execute(adicionar, (id, plato, marca, valor))

    # Commit das mudanças
    #conexao.commit()

    # Exemplo de consulta SELECT
    #query = "SELECT * FROM estoque"
    #cursor.execute(query)

    # Obter todos os resultados da consulta
    #resultados = cursor.fetchall()

    # Exibir os resultados
    #for linha in resultados:
        #print(linha)

#except mysql.connector.Error as erro:
    #print(f"Erro MySQL: {erro}")

#except Exception as e:
    #print(f"Erro: {e}")

#finally:
    # Fechar o cursor e a conexão
    #cursor.close()
    #conexao.close()
