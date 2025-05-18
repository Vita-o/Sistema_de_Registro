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

# ================================== Criando Caixas de entraa ==================================
l_usuario = Label(frame_logo, text="Usuario*", anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_usuario.place(x=75, y=5)
e_usuario = Entry(frame_logo, width=25, justify='left', relief='solid')
e_usuario.place(x=75, y=25)

l_senha = Label(frame_logo, text="Senha*", anchor=NW, font=('Ivy 8'), bg=co1, fg=co4)
l_senha.place(x=75, y=50)
e_senha = Entry(frame_logo, width=25, justify='left', relief='solid')
e_senha.place(x=75, y=70)




# ================================== Criando Mudança de Tela ==================================
# Assuming sistema_de_usuario is an instance of your user system class
# and e_usuario and e_senha are your entry widgets
def redefiniir_senha(usuario_digitado, senha_digitada):

    usuario_digitado = e_usuario.get()
    senha_digitada = e_senha.get()

    usuario_banco = sistema_de_usuario.confirmar_usuario(usuario_digitado)

    frame_mudar_senha = Frame(janela, width=300, height=240, bg=co1, relief=SOLID)
    frame_mudar_senha.grid(row=3, column=1, pady=10, padx=0, sticky=NSEW)


    # Função para pegar o nome de usuário e escrever na tela
    def salvar_senha():
        
        senha_antiga = e_senha_ant.get()
        senha1 = e_senha1.get()
        senha2 = e_senha2.get()

        if senha_digitada == senha_antiga:
        
            if senha1 == senha2:

                sistema_de_usuario.atualizar_senha(usuario_digitado,senha1)
                janela.destroy()
                subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telalogin.py'])

            else:
                messagebox.showinfo("ERRO", "SENHA NÃO SÃO IGUAIS")
        else:
            messagebox.showinfo("ERRO","Senha Antiga não confere")



    # ================================== Criando Caixas de entraa ==================================
    l_usuario = Label(frame_mudar_senha, text=f"{usuario_digitado}", justify='center', anchor=CENTER, font=('Ivy 10'), bg=co1, fg=co4)
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
           
            redefiniir_senha(usuario_digitado, senha_digitada)

        elif usuario_digitado == nome_banco and senha_digitada == senha_banco and cargo_banco == "ADMINISTRATIVO":

            janela.destroy()
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telaregistro.py'])

        elif usuario_digitado == nome_banco and senha_digitada == senha_banco and cargo_banco == "PROFESSOR":
            
            janela.destroy()
            subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'teladeusuarios.py'])

        else:
            messagebox.showerror("Erro", "Senha incorreta.")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.") # Replace with proper GUI error handling



# ================================== Criando Botão ==================================
b_login = Button(frame_logo, width=18, command=confirmarusuario, relief=GROOVE, text=' Login ', compound=LEFT, overrelief=RIDGE, font=('Ivy 10'), bg=co0, fg=co1)
b_login.place(x=75, y=110)

janela.mainloop()