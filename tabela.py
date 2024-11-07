from tkinter import *
from tkinter import ttk
from datetime import datetime

def centralizar_janela(janela, largura, altura):
    
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def interface():

    janela = Tk()
    janela.title("Tabela")
    janela.geometry("800x500")

    frame = Frame(janela)
    frame.pack(expand=True)

    table = ttk.Treeview(frame, columns=("Data", "Descricao", "Sentido", "Categoria", "Valor"), show="headings")
    
    # Definindo nomes das colunas e larguras
    table.heading("Data", text="Data")
    table.heading("Descricao", text="Descricao")
    table.heading("Sentido", text="Sentido")
    table.heading("Categoria", text="Categoria")
    table.heading("Valor", text="Valor")
    
    table.column("Data", width=100, anchor=CENTER)
    table.column("Descricao", width=200, anchor=W)
    table.column("Sentido", width=60, anchor=CENTER)
    table.column("Categoria", width=150, anchor=W)
    table.column("Valor", width=100, anchor=W)

    vsb = ttk.Scrollbar(frame, orient="vertical", command=table.yview)

    table.configure(yscroll=vsb.set)
    table.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    dados = __import__('sgf').ler_banco()

    fdados = []

    for linha in dados:
        data, descricao, sentido, categoria, valor = linha
        data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
        fdados.append((data, descricao, sentido, categoria, valor))

    for item in fdados:
        table.insert("", "end", values=item)

    centralizar_janela(janela, 800, 500)

    janela.mainloop()

if __name__ == "__main__":
    interface()