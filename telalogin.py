# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess

# importando pillow
from PIL import ImageTk, Image


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

frame_logo = Frame(janela, width=300, height=150, bg=co1, relief=SOLID)
frame_logo.grid(row=3, column=1, pady=10, padx=0, sticky=NSEW)

# ================================== Criando Mudança de Tela ==================================
# Assuming sistema_de_usuario is an instance of your user system class
# and e_usuario and e_senha are your entry widgets


def confirmarusuario():

    usuario_digitado = e_usuario.get()
    senha_digitada = e_senha.get()

    usuario_banco = sistema_de_usuario.confirmar_usuario(usuario_digitado)

    if usuario_digitado == 'Admin' and senha_digitada == 'Admin':
        janela.destroy()
        subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'teladeusuarios.py'])
    elif usuario_banco:
        nome_banco, senha_banco, caixa_banco, cargo_banco = usuario_banco

        if int(caixa_banco) == 1: # Convertemos para inteiro para comparar
            janela.destroy()
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telanovasenha.py', usuario_digitado, senha_digitada])
        elif usuario_digitado == nome_banco and senha_digitada == senha_banco and cargo_banco == "ADMINISTRATIVO":

            janela.destroy()
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telaregistro.py'])

        elif usuario_digitado == nome_banco and senha_digitada == senha_banco and cargo_banco == "PROVESSOR":
            
            janela.destroy()
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'teladeusuarios.py'])

        else:
            messagebox.showerror("Erro", "Senha incorreta.")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.") # Replace with proper GUI error handling


# ================================== Criando Caixas de entraa ==================================
l_usuario = Label(frame_logo, text="Usuario*", anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_usuario.place(x=75, y=5)
e_usuario = Entry(frame_logo, width=25, justify='left', relief='solid')
e_usuario.place(x=75, y=25)

l_senha = Label(frame_logo, text="Senha*", anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_senha.place(x=75, y=50)
e_senha = Entry(frame_logo, width=25, justify='left', relief='solid')
e_senha.place(x=75, y=70)

# ================================== Criando Botão ==================================
b_login = Button(frame_logo, width=18, command=confirmarusuario, relief=GROOVE, text=' Login ', compound=LEFT, overrelief=RIDGE, font=('Ivy 10'), bg=co0, fg=co1)
b_login.place(x=75, y=110)

janela.mainloop()