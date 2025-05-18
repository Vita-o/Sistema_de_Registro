# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess

# importando pillow
from PIL import ImageTk, Image
import sys

# importando sistema de usuari
from sistemadeusuarios import sistema_de_usuario

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co1 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#003452"  # azul
co7 = "#ef5350"  # vermelha

co6 = "#146C94"  # azul
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde


janela = Tk()
janela.title('Login')
janela.geometry("810x535")
janela.configure(background=co6)
janela.resizable(width=TRUE, height=TRUE)

style = Style(janela)
style.theme_use("classic")


# ================================== Criando Frames ==================================

# Configurando pesos para as colunas e linhas da janela para centralizar
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(3, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(4, weight=1)

frame_mudar_senha = Frame(janela, width=300, height=240, bg=co1, relief=SOLID)
frame_mudar_senha.grid(row=3, column=1, pady=10, padx=0, sticky=NSEW)

# ================================== Criando Funções ==================================

nome_usuario = None
if len(sys.argv) > 1:
    nome_usuario = sys.argv[1]
    senha_usuario = sys.argv[2]

# Função para pegar o nome de usuário e escrever na tela
def salvar_senha():

    senha1 = e_senha1.get()
    senha2 = e_senha2.get()

    if e_senha_ant.get() == senha_usuario:
    
        if senha1 == senha2:

            sistema_de_usuario.atualizar_senha(nome_usuario,senha1)
            janela.destroy()         
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telalogin.py'])


        else:
            messagebox.showinfo("ERRO", "SENHA NÃO SÃO IGUAIS")
    else:
        messagebox.showinfo("ERRO","Senha Antiga não confere")



# ================================== Criando Caixas de entraa ==================================
l_usuario = Label(frame_mudar_senha, text=f"{nome_usuario}", justify='center', anchor=CENTER, font=('Ivy 10'), bg=co1, fg=co4)
l_usuario.place(x=0, y=10, width=300)

l_senha_ant = Label(frame_mudar_senha, text="Senha Antiga*", justify='left', anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_senha_ant.place(x=75, y=40)
e_senha_ant = Entry(frame_mudar_senha , width=25, justify='left', relief='solid')
e_senha_ant.place(x=75, y=60)

l_senha1 = Label(frame_mudar_senha, text="Nova Senha*", justify='left', anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_senha1.place(x=75, y=90)
e_senha1 = Entry(frame_mudar_senha, width=25, justify='left', relief='solid')
e_senha1.place(x=75, y=110)

l_senha2 = Label(frame_mudar_senha, text="Confirmar Senha*", justify='left', anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_senha2.place(x=75, y=140)
e_senha2 = Entry(frame_mudar_senha, width=25, justify='left', relief='solid')
e_senha2.place(x=75, y=160)


# ================================== Criando Botão ==================================
b_salvarsenha = Button(frame_mudar_senha, width=18, command=salvar_senha, relief=GROOVE, text=' Login ', compound=LEFT, overrelief=RIDGE, font=('Ivy 10'), bg=co0, fg=co1)
b_salvarsenha.place(x=75, y=200)

janela.mainloop()