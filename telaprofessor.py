#importando dependencias do Tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando Sistem De Estudante
from sistemadeusuarios import *


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co1 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#================================== Criando Janela ==================================
janela = Tk()
icone = tk.PhotoImage(file='Icones/Logo.png')
janela.iconphoto(False, icone)
janela.title("Registro De Faltas")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("alt")

# ================================== Criando Frames ==================================
frame_logo = Frame(janela, width=810, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW,columnspan=5)


#================================== Frame Logo ==================================
global imagem, imagem_string, l_imagem

def sair():
    janela.destroy()


app_lg = Image.open('Icones/Logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Registro de Faltas ", width=740, compound=LEFT, anchor=CENTER, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW) 


b_sair = Button(frame_logo, text='EXIT', command=sair, width= 6, font=('Ivy 10'), bg=co1, fg=co0)
b_sair.grid(row=0, column=5, pady=0, padx=2, sticky=NSEW) 

#================================== Abrindo Imagem usuario ==================================
imagem = Image.open('Icones/aluno.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)

#================================== Criando funçoes para CRUD ==================================
# Adicionar
def adicionar():
    
    global imagem, imagem_string, l_imagem, a_caixa


    #obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    cargo = c_cargo.get()
    data = data_nascimento.get()
    endereco = c_endereco.get()
    materia = c_materia.get()
    senha = c_senha.get()
    caixa = a_caixa.get()
    img = imagem_string
    
    lista = [nome, email, tel, sexo, cargo, data, endereco, materia, senha, caixa, img]

    # verificando se tem Volar Vazio
    for i in lista:
        if i=='':
            messagebox.showerror("Erro", f"Preencha todos os campos {lista}")
            return
    # registrando os valores
    sistema_de_usuario.register_usuario(lista)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_cargo.delete(0, END)
    data_nascimento.delete(0, END)
    c_endereco.delete(0, END)
    c_materia.delete(0, END)
    c_senha.delete(0, END)

    a_caixa = tk.BooleanVar(value=True)
    c_caixa = ttk.Checkbutton(frame_details, text="Mudar senha ao Entrar", variable=a_caixa, command=realizar_acao)
    c_caixa.place(x=224, y=205)
 
    imagem = Image.open('Icones/aluno.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)
    
    # Mostrando os valores da tabela
    mostrar_usuarios()

# Procurar usuario
def procurar():
    global imagem, imagem_string, l_imagem, a_caixa

    # obtendo id
    id_usuario = int(e_procurar.get())

    #procurar usuario
    dados = sistema_de_usuario.search_usuario(id_usuario)

        # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_cargo.delete(0, END)
    data_nascimento.delete(0, END)
    c_endereco.delete(0, END)
    c_materia.delete(0, END)
    c_senha.delete(0, END)


        # Inserindo Valores Novos
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    c_cargo.insert(END, dados[5])
    data_nascimento.insert(END, dados[6])
    c_endereco.insert(END, dados[7])
    c_materia.insert(END, dados[8])
    c_senha.insert(END,dados[9])
    
    a_caixa = tk.BooleanVar(value=dados[10])
    c_caixa = ttk.Checkbutton(frame_details, text="Mudar senha ao Entrar", variable=a_caixa, command=realizar_acao)
    c_caixa.place(x=224, y=205)
    
    imagem = dados[11]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)


#  Atualizar 
def atualizar():
    global imagem, imagem_string, l_imagem, a_caixa

    # obtendo id
    id_usuario = int(e_procurar.get())


    #obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    cargo = c_cargo.get()
    data = data_nascimento.get()
    endereco = c_endereco.get()
    materia = c_materia.get()
    senha = c_senha.get()
    caixa = a_caixa.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, cargo, data, endereco, materia, senha, caixa, img, id_usuario]

    # verificando se tem Volar Vazio
    for i in lista:
        if i=='':
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    # registrando os valores
    sistema_de_usuario.update_usuario(lista)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_cargo.delete(0, END)
    data_nascimento.delete(0, END)
    c_endereco.delete(0, END)
    c_materia.delete(0, END)
    c_senha.delete(0, END)
    a_caixa.delete(0,END)

    a_caixa = tk.BooleanVar(value=True)
    c_caixa = ttk.Checkbutton(frame_details, text="Mudar senha ao Entrar", variable=a_caixa, command=realizar_acao)
    c_caixa.place(x=224, y=205)    

# Abrindo A imagem
    imagem = Image.open('Icones/aluno.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # Mostrando os valores da tabela
    mostrar_usuarios()

# Deletar usuario
def deletar():
    global imagem, imagem_string, l_imagem, a_caixa

    # obtendo id
    id_usuario = int(e_procurar.get())

    # Deletando usuario
    sistema_de_usuario.delet_usuario(id_usuario)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_cargo.delete(0, END)
    data_nascimento.delete(0, END)
    c_endereco.delete(0, END)
    c_materia.delete(0, END)
    c_senha.delete(0, END)

    a_caixa = tk.BooleanVar(value=True)
    c_caixa = ttk.Checkbutton(frame_details, text="Mudar senha ao Entrar", variable=a_caixa, command=realizar_acao)
    c_caixa.place(x=224, y=205)

# Abrindo A imagem
    imagem = Image.open('Icones/usuario.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)
       
    # Mostrando os valores da tabela
    mostrar_usuarios()

# Funcao pra Habilita e desabilitar Materia
def selecionar_cargo(event):
    cargo_selecionado = c_cargo.get()
    if cargo_selecionado == "ADMINISTRATIVO":
        c_materia.config(state=DISABLED)
        l_materia.config(state=DISABLED)
        c_materia.set('DESABILITADO')
    else:
        c_materia.set('')
        c_materia.config(state=NORMAL)
        l_materia.config(state=NORMAL)
        c_materia['values'] = (cursos)


def realizar_acao(event=None):
    if a_caixa.get() == True:
        print(f"Opção marcada! Realizando ação... {a_caixa.get()}")
    else:
        print(f"Opção desmarcada. {a_caixa.get()}")


# ================================== Campos de Entrada ==================================
l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=35)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=60)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=85)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=110)
e_tel = Entry(frame_details, width=18, justify='left', relief='solid')
e_tel.place(x=7, y=135)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=110)
c_sexo = ttk.Combobox(frame_details, width=7, font=('Ivy 8'),justify='center')
c_sexo['values'] = ('MASCULINO', 'FEMININO')
c_sexo.place(x=130, y=135)


l_carcgo = Label(frame_details, text="Cargo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_carcgo.place(x=4, y=160)
c_cargo = ttk.Combobox(frame_details, width=25, font=('Ivy 8'),justify='center')
c_cargo['values'] = ('PROFESSOR', 'ADMINISTRATIVO')
c_cargo.place(x=4, y=185)
c_cargo.bind("<<ComboboxSelected>>", selecionar_cargo)


l_data_nascimento = Label(frame_details, text="Data De Nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=11, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
data_nascimento.place(x=224, y=35)

l_endereco = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=60)
c_endereco = Entry(frame_details, width=20, justify='left', relief='solid')
c_endereco.place(x=224, y=85)

# Criando Cursos

cursos = ['Engenharia', 'Medicina', 'Administração']

l_materia = Label(frame_details, text="Materia *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_materia.place(x=220, y=110)
c_materia = ttk.Combobox(frame_details, width=20, font=('Ivy 8'),justify='center')

c_materia['values'] = (cursos)
c_materia.place(x=224, y=135)

l_senha = Label(frame_details, text="Senha *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_senha.place(x=220, y=160)
c_senha = Entry(frame_details, width=25, justify='left', relief='solid')
c_senha.place(x=224, y=185)

a_caixa = tk.BooleanVar(value=True)
c_caixa = ttk.Checkbutton(frame_details, text="Mudar senha ao Entrar", variable=a_caixa, command=realizar_acao)
c_caixa.place(x=224, y=205)

#================================== Função para escolher imagem ==================================

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar De Foto'


botao_carregar = Button(frame_details,command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)


# Criando tabelas de usuarios
def mostrar_usuarios():

    #
    list_header = ['id', 'Nome', 'Cargo', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Materia']

    df_list= sistema_de_usuario.view_all_usuario()

    tree_usuario = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # Definindo os cabeçalhos das colunas
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_usuario.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_usuario.xview)

    tree_usuario.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    # Posicionando a Treeview e as barras de rolagem
    tree_usuario.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    # Configurando o peso das linhas e colunas do frame para que a Treeview se expanda
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", 'center', 'center', 'center', 'center', 'center']
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_usuario.heading(col, text=col.title(), anchor=NW)
        tree_usuario.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:   
        tree_usuario.insert('', 'end', values=item)        
        # Adicione esta linha para exibir a tabela ao iniciar o programa
    return tree_usuario

#================================== Procurar usuario ==================================
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar usuario [Entra ID] *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_alterar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_alterar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)


#================================== Botoes =================================

app_img_adicionar = Image.open('Icones/Add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, relief=GROOVE, text=' Adicionar ', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)


app_img_atualizar = Image.open('Icones/update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=' Atualizar ', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)


app_img_deletar = Image.open('Icones/Delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, relief=GROOVE, text=' Deletar ', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Linha Separatoria
l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co0, fg=co1)
l_linha.place(x=240, y=15)

# Chamando a função para criar e exibir a tabela
mostrar_usuarios()

janela.mainloop()

