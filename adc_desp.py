from tkinter import *

def valida_entrada(char):
    return char.isdigit() or char == '.' or char == ''

def interface():

    janela = Tk()
    janela.title("Adicionar despesa")
    janela.geometry("300x250")

    validacao_numeros = janela.register(valida_entrada)

    frame = Frame(janela)
    frame.pack(expand=True)

    frame.grid_columnconfigure(0, weight=0)

    texto = Label(frame, text="Adicionar despesa")
    texto.grid(column=0, row=1, sticky="ew")

    linha_branco = Label(frame, text="")
    linha_branco.grid(column=0, row=2)

    texto2 = Label(frame, text="Descrição")
    texto2.grid(column=0, row=3, sticky="ew")

    in_descr = Text(frame, width=30, height=1)
    in_descr.grid(column=0, row=4, sticky="ew")

    texto3 = Label(frame, text="Categoria")
    texto3.grid(column=0, row=5, sticky="ew")

    in_categ = Text(frame, width=30, height=1)
    in_categ.grid(column=0, row=6, sticky="ew")

    texto4 = Label(frame, text="Valor")
    texto4.grid(column=0, row=7, sticky="ew")

    in_valor = Entry(frame, validate="key", validatecommand=(validacao_numeros, '%S'))
    in_valor.grid(column=0, row=8, sticky="ew")

    linha_branco = Label(frame, text="")
    linha_branco.grid(column=0, row=9)

    botao = Button(frame, text="Adicionar", command=lambda: (__import__('sgf').adiciona_despesa(in_descr.get(1.0, "end-1c"), in_categ.get(1.0, "end-1c"), in_valor.get()), janela.destroy()), width=20)
    botao.grid(column=0, row=10, padx=10, pady=10, sticky="ew")

    janela.mainloop()

if __name__ == "__main__":
    interface()