from tkinter import *
import string
from random import choice
import clipboard as clipboard

window = Tk()


class Funcoes():
    def gerarSenha(self):
        val = string.ascii_letters  # letras
        val += string.digits  # números
        tam = 8  # tamanho da senha
        senha = ''
        for i in range(tam):
            senha += choice(val)
        self.res['text'] = senha

    def copiar(self):
        copiar = clipboard.copy(self.res['text'])
        self.bt_copiar['text'] = 'Copiado!'


class Aplicacao(Funcoes):
    def __init__(self):
        self.window = window
        self.tela()
        self.frametela()
        self.botoes()
        self.textos()
        self.saida()
        window.mainloop()

    def tela(self):
        self.window.title("Gerador de Senhas")  # titulo
        self.window.configure(background='#F2AF29')  # cor de fundo
        self.window.geometry("500x300")  # tamanho inicial da tela
        self.window.resizable(True, True)  # Responsividade Altura e Largura
        self.window.maxsize(width=750, height=420)  # tamanho máximo da tela permitido
        self.window.minsize(width=450, height=250)  # tamanho mínimo da tela permitido

    def frametela(self):
        self.frame1 = Frame(self.window, bd=4, bg='#e7e7e7', highlightbackground='#000',
                            highlightthickness=2)
        self.frame1.place(relx=0.13, rely=0.13, relwidth=0.7, relheight=0.7 )
        # o relx e rely é responsivo pois é relativo ao tamanho da tela.

    def botoes(self):
        # botoes gerar senha e copiar
        self.bt_gerar = Button(self.frame1, text='Gerar Senha', bg='#EC368D', fg='white',
                               font=('verdana', 9), command=self.gerarSenha)
        self.bt_gerar.place(relx=0.1, rely=0.8, relwidth=0.3, relheight=0.15)
        self.bt_copiar = Button(self.frame1, text='Copiar', bg='#F16AAB', fg='white',
                                font=('verdana', 9), command=self.copiar)
        self.bt_copiar.place(relx=0.57, rely=0.8, relwidth=0.3, relheight=0.15)

    def textos(self):
        self.lbsenha = Label(self.frame1, text='Senha:', bg='#e7e7e7', font=('verdana', 14))
        self.lbsenha.place(relx=0.14, rely=0.15)

    def saida(self):
        # caixa onde será mostrado o resultado
        self.res = Label(self.frame1, text='', bg='white', font=('verdana', 12))
        self.res.place(relx=0.14, rely=0.35, relwidth=0.72, relheight=0.3)


Aplicacao()
