from tkinter import *
import os
import sqlite3
from datetime import datetime

db_path = "C:\\Users\\cs406463\\Downloads\\sgf.db"
banco_existe = os.path.exists(db_path)

def interface():

    global texto3
    
    janela = Tk()
    janela.title("SGF")
    janela.geometry("800x600")

    janela.grid_columnconfigure(0, weight=1)

    texto = Label(janela, text="SGF - Sistema de Gestão Financeira")
    texto.grid(column=0, row=1, sticky="ew")

    texto2 = Label(janela, text="Bem vindo, USER")
    texto2.grid(column=0, row=2, sticky="w")

    linha_branco = Label(janela, text="")
    linha_branco.grid(column=0, row=3)

    texto3 = Label(janela, text="Seu saldo é: " + str(ler_saldo()[0][0]))
    texto3.grid(column=0, row=4, sticky="w")

    texto4 = Label(janela, text="Você tem X ações para hoje.")
    texto4.grid(column=0, row=5, sticky="w")

    linha_branco = Label(janela, text="")
    linha_branco.grid(column=0, row=6)

    botao = Button(janela, text="Adcionar despesa", command=lambda: __import__('adc_desp').interface(), width=20)
    botao.grid(column=0, row=7, padx=0, pady=0, sticky="w")

    botao2 = Button(janela, text="Adcionar entradas", command=lambda: __import__('adc_entr').interface(), width=20)
    botao2.grid(column=0, row=8, padx=0, pady=0, sticky="w")

    botao2 = Button(janela, text="Tabela", command=lambda: __import__('tabela').interface(), width=20)
    botao2.grid(column=0, row=9, padx=0, pady=0, sticky="w")

    centralizar_janela(janela, 800, 600)

    janela.mainloop()

def checa_banco():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if not banco_existe:

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS despesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                descricao TEXT,
                sentido TEXT,
                categoria TEXT,
                valor REAL
            )
        ''')

    cursor.execute("PRAGMA table_info(despesas)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "data" not in colunas:
        cursor.execute("ALTER TABLE despesas ADD COLUMN data TEXT")

    if "descricao" not in colunas:
        cursor.execute("ALTER TABLE despesas ADD COLUMN descricao TEXT")

    if "sentido" not in colunas:
        cursor.execute("ALTER TABLE despesas ADD COLUMN sentido TEXT")

    if "categoria" not in colunas:
        cursor.execute("ALTER TABLE despesas ADD COLUMN categoria TEXT")

    if "valor" not in colunas:
        cursor.execute("ALTER TABLE despesas ADD COLUMN valor REAL")

    conn.commit()
    conn.close()

def adiciona_banco(data, descricao, sentido, categoria, valor):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO despesas (data, descricao, sentido, categoria, valor) VALUES (?, ?, ?, ?, ?)", 
               (data, descricao, sentido, categoria, valor))
    
    conn.commit()
    conn.close()

def adiciona_despesa(descricao, categoria, valor):
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    adiciona_banco(data_atual, descricao, "Despesa", categoria, valor)

def adiciona_entrada(descricao, categoria, valor):
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    adiciona_banco(data_atual, descricao, "Entrada", categoria, valor)

def ler_banco():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT data, descricao, sentido, categoria, valor FROM despesas")
    dados = cursor.fetchall()

    return dados

def ler_saldo():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(CASE WHEN sentido = 'Entrada' THEN valor ELSE 0 END) - SUM(CASE WHEN sentido = 'Despesa' THEN valor ELSE 0 END) AS saldo FROM despesas")
    saldo = cursor.fetchall()

    return saldo

def upd_saldo(texto3):

    texto3.config(text="Seu saldo é: " + str(ler_saldo()[0][0]))
    

def centralizar_janela(janela, largura, altura):
    
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

if __name__ == "__main__":
    
    checa_banco()
    interface()