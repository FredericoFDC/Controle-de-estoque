import mysql.connector
from ConeccaoComBanco import criar_conexao

def obter_info_peca(nome_peca):
    try:
        # Criar uma conexão
        conexao = criar_conexao()

        # Criar um cursor para interagir com o banco de dados
        cursor = conexao.cursor()

        # Verificar se a peça já existe no estoque
        sql_select = "SELECT valor FROM plato WHERE plato = %s"
        cursor.execute(sql_select, (nome_peca,))
        resultado = cursor.fetchone()

        if resultado:
            # Consumir todos os resultados antes de prosseguir
            cursor.fetchall()

            return resultado[0]

        else:
            print("Erro: Peça não encontrada no estoque.")
            return None

    except mysql.connector.Error as erro:
        print(f"Erro MySQL: {erro}")
        return None

    except Exception as e:
        print(f"Erro: {e}")
        return None

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

def alterar_valor(nome_peca, novo_valor):
    # Obter informações sobre a peça (incluindo o valor atual)
    info_peca = obter_info_peca(nome_peca)

    if info_peca is not None:
        valor_atual = info_peca
        print(f"Valor atual da peça '{nome_peca}': {valor_atual}")

        try:
            # Criar uma conexão
            conexao = criar_conexao()

            # Criar um cursor para interagir com o banco de dados
            cursor = conexao.cursor()

            # Atualizar o valor da peça no estoque
            sql_update = "UPDATE plato SET valor = %s WHERE plato = %s"
            cursor.execute(sql_update, (novo_valor, nome_peca))

            # Commit da transação
            conexao.commit()

            print(f"O valor da peça '{nome_peca}' foi atualizado para {novo_valor}.")

        except mysql.connector.Error as erro:
            print(f"Erro MySQL: {erro}")

        except Exception as e:
            print(f"Erro: {e}")

        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

# Exemplo de uso da função para alterar o valor de uma peça
while True:
    nome_peca_alterar_valor = input("Digite o nome da peça: ")
    novo_valor_peca = float(input("Digite o novo valor para a peça: "))
    alterar_valor(nome_peca_alterar_valor, novo_valor_peca)
