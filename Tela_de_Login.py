# Dados fictícios para servir como banco de dados
banco_de_dados = {
    "axor": {"plato": 600, "disco": 200, "rolamento": 200}
}

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Credenciais de login
credenciais = {"usuario": "admin", "senha": "1234"}

# Variável para armazenar o campo de pesquisa
campo_pesquisa = None

# Função para verificar o login e senha
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == credenciais["usuario"] and senha == credenciais["senha"]:
        messagebox.showinfo("Login", "Login bem-sucedido")
        janela_login.destroy()
        abrir_janela_principal()
    else:
        messagebox.showerror("Login", "Credenciais inválidas")

# Função para abrir a janela principal após o login bem-sucedido
def abrir_janela_principal():
    janela_principal = tk.Tk()
    janela_principal.title("Controle de Estoque")
    janela_principal.geometry("800x600")

    rótulo = tk.Label(janela_principal, text="Olá, Mundo!")
    rótulo.pack()

    # Adicionar um campo de pesquisa
    global campo_pesquisa  # Declare campo_pesquisa como global
    campo_pesquisa = tk.Entry(janela_principal)
    campo_pesquisa.pack()

    # Adicionar um botão de pesquisa
    botao_pesquisar = tk.Button(janela_principal, text="Pesquisar", command=executar_pesquisa)
    botao_pesquisar.pack()

# Função para executar a pesquisa
def executar_pesquisa():
    global campo_pesquisa  # Declare campo_pesquisa como global
    termo_pesquisa = campo_pesquisa.get().lower()

    resultado_pesquisa = []
    for item in banco_de_dados:
        if termo_pesquisa in item.lower():
            resultado_pesquisa.append(item)

    # Exiba os resultados da pesquisa
    resultado = "Resultados da pesquisa:\n"
    for item in resultado_pesquisa:
        resultado += f"Produto: {item}, Estoques: {banco_de_dados[item]}\n"

    messagebox.showinfo("Pesquisa", resultado)

# Janela de login
janela_login = tk.Tk()
janela_login.title("Login")

# Defina a geometria da janela de login para 800x500 pixels e centralize
largura_janela = 800
altura_janela = 500
largura_tela = janela_login.winfo_screenwidth()
altura_tela = janela_login.winfo_screenheight()
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2
janela_login.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

# Crie um quadro para o formulário
quadro = tk.Frame(janela_login)
quadro.pack(pady=180)

# Rótulos para os campos de entrada
rótulo_usuario = tk.Label(quadro, text="Usuário:")
rótulo_senha = tk.Label(quadro, text="Senha:")

entrada_usuario = tk.Entry(quadro)
entrada_senha = tk.Entry(quadro, show="*")

rótulo_usuario.grid(row=0, column=0, padx=10, pady=10)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

rótulo_senha.grid(row=1, column=0, padx=10, pady=10)
entrada_senha.grid(row=1, column=1, padx=10, pady=10)

# Botão de login
botao_login = tk.Button(quadro, text="Login", command=verificar_login)
botao_login.grid(row=2, columnspan=2, padx=10, pady=10)

janela_login.mainloop()
