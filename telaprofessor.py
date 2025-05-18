#importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess
import sys

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando Sistem De Estudante
from sistemaderegistro import *
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
janela.title("")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("alt")

# ================================== Criando Frames ==================================
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10,columnspan=5)

# configurando tamanho da tabela fixo
frame_tabela.grid_rowconfigure(0, weight=1)
frame_tabela.grid_columnconfigure(0, weight=1)

tree_alunos = None
estados_checkboxes = {}
professor_logado_id = None # Inicializa como None

# Verifique se um ID de professor foi passado como argumento
if len(sys.argv) > 1:
    try:
        professor_logado_id = int(sys.argv[1])
    except ValueError:
        messagebox.showerror("Erro", "ID do professor inválido.")
        janela.destroy()
        sys.exit()
else:
    messagebox.showerror("Erro", "ID do professor não fornecido.")
    janela.destroy()
    sys.exit()
#================================== Frame Logo ==================================
global imagem, imagem_string, l_imagem

def sair():
    janela.destroy()


app_lg = Image.open('Icones/Logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Registro de Aluno ", width=740, compound=LEFT, anchor=CENTER, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW) 


b_sair = Button(frame_logo, text='EXIT', command=sair, width= 6, font=('Ivy 10'), bg=co1, fg=co0)
b_sair.grid(row=0, column=5, pady=0, padx=2, sticky=NSEW) 
#================================== Abrindo Imagem Aluno ==================================
imagem = Image.open('Icones/aluno.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)

#================================== Criando funçoes para CRUD ==================================
# Adicionar
def adicionar():
    
    global imagem, imagem_string, l_imagem
    imagem_string = ''

    #obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string
    
    lista = [nome, email, tel, sexo, data, endereco, curso, img]

    # verificando se tem Volar Vazio
    for i in lista:
        if i=='':
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    # registrando os valores
    sistema_de_registro.register_studant(lista)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)


    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # Mostrando os valores da tabela
    mostrar_alunos()

# Procurar Aluno
def procurar():
    global imagem, imagem_string, l_imagem

    # obtendo id
    id_aluno = int(e_procurar.get())

    #procurar aluno
    dados = sistema_de_registro.search_studant(id_aluno)

        # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

        # Limpando campo de entrada
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)


#  Atualizar 
def atualizar():
    global imagem, imagem_string, l_imagem

    # obtendo id
    id_aluno = int(e_procurar.get())


    #obtendo valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

    # verificando se tem Volar Vazio
    for i in lista:
        if i=='':
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    # registrando os valores
    sistema_de_registro.update_student(lista)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

# Abrindo A imagem
    imagem = Image.open('Icones/aluno.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # Mostrando os valores da tabela
    mostrar_alunos()

# Deletar Aluno
def deletar():
    global imagem, imagem_string, l_imagem

    # obtendo id
    id_aluno = int(e_procurar.get())

    # Deletando aluno
    sistema_de_registro.delet_student(id_aluno)

    # Limpando campo de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

# Abrindo A imagem
    imagem = Image.open('Icones/aluno.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)
       
    # Mostrando os valores da tabela
    mostrar_alunos()


# ================================== Campos de Entrada ==================================
l_nome = Label(frame_details, text="Nome Do Aluno Completo*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=18, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=('Ivy 8'),justify='center')
c_sexo['values'] = ('MASCULINO', 'FEMININO')
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_details, text="Data De Nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=11, background='darkblue', foreground='white', borderwidth=2)
data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_details, width=20, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

# Criando Cursos
cursos = ['Engenharia', 'Medicina', 'Administração']

l_curso = Label(frame_details, text="Cursos *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=20, font=('Ivy 8'),justify='center')
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)

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



tree_alunos = None  # Variável global para a Treeview
estados_checkboxes = {} # Dicionário para guardar o estado dos checkboxes



def obter_materia_professor(professor_id):
    """Obtém a matéria do professor logado."""
    dados_professor = sistema_de_usuario.search_usuario(professor_id)
    if dados_professor and len(dados_professor) > 8: # Verifica se a matéria existe
        return dados_professor[8] # A matéria está na nona posição (índice 8)
    return None

def mostrar_alunos():
    global tree_alunos, estados_checkboxes, materia_professor, professor_logado_id

    materia_professor = obter_materia_professor(professor_logado_id)

    if not materia_professor:
        messagebox.showerror("Erro", "Não foi possível obter a matéria do professor.")
        return

    list_header = ['ID', 'Nome'] + [f'Dia {i+1}' for i in range(25)]

    if tree_alunos:
        tree_alunos.destroy()
        estados_checkboxes = {} # Limpar os estados ao mostrar novamente

    tree_alunos = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
    tree_alunos.grid(row=0, column=0, sticky="nsew")
    # Definindo os cabeçalhos
    tree_alunos.heading('ID', text='ID', anchor='center')
    tree_alunos.column('ID', width=40, anchor='center')
    tree_alunos.heading('Nome', text='Nome', anchor='nw')
    tree_alunos.column('Nome', width=150, anchor='nw')
    for i in range(25):
        tree_alunos.heading(f'Dia {i+1}', text='', anchor='center')
        tree_alunos.column(f'Dia {i+1}', width=30, anchor='center')

    # Adicionando barras de rolagem
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_alunos.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_alunos.xview)
    tree_alunos.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_alunos.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    # Definindo os cabeçalhos
    tree_alunos.heading('ID', text='ID', anchor='center')
    tree_alunos.column('ID', width=50, anchor='center', stretch=NO)
    tree_alunos.heading('Nome', text='Nome', anchor='nw')
    tree_alunos.column('Nome', width=150, anchor='nw', stretch=NO)
    for i in range(25):
        tree_alunos.heading(f'Dia {i+1}', text='', anchor='center')
        tree_alunos.column(f'Dia {i+1}', width=30, anchor='center', stretch=NO)


    # Inserir dados
    alunos_da_materia = sistema_de_registro.get_alunos_por_materia(materia_professor)

    for aluno in alunos_da_materia:
        aluno_id = aluno[0]
        nome_aluno = aluno[1]
        values = [aluno_id, nome_aluno] + ['[ ]' for _ in range(25)]
        tree_alunos.insert('', 'end', values=values)
        estados_checkboxes[aluno_id] = [False] * 25 # Inicializa o estado dos checkboxes

    tree_alunos.bind('<Button-1>', on_treeview_click)
    return tree_alunos

def on_treeview_click(event):
    global tree_alunos, estados_checkboxes
    item_id = tree_alunos.identify_row(event.y)
    column_id = tree_alunos.identify_column(event.x)

    if item_id and column_id not in ('#0', '#1'):  # Ignora a coluna de ID e Nome
        col_index = int(column_id[1:]) - 2  # Ajusta o índice para corresponder à lista de estados
        aluno_id = tree_alunos.item(item_id, 'values')[0]

        if aluno_id in estados_checkboxes:
            current_state = estados_checkboxes[aluno_id][col_index]
            estados_checkboxes[aluno_id][col_index] = not current_state
            novo_marcador = '[X]' if estados_checkboxes[aluno_id][col_index] else '[ ]'
            tree_alunos.set(item_id, column_id, novo_marcador)
#================================== Procurar Aluno ==================================
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar Aluno [Entra ID] *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
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
mostrar_alunos()

janela.mainloop()