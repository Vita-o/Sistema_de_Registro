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

if len(sys.argv) > 1:
    pass

else:
    janela.destroy()
    messagebox.showerror("Erro", "Usuario nao Logado.")
    sys.exit()
# ================================== Criando Frames ==================================
frame_logo = Frame(janela, width=850, height=52, bg=co6)
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
        subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telalogin.py'])



app_lg = Image.open('Icones/Logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Registro de Aluno ", width=740, compound=LEFT, anchor=CENTER, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW) 


b_sair = Button(frame_logo, text='EXIT', command=sair, width= 6, font=('Ivy 10'), bg=co1, fg=co0)
b_sair.grid(row=0, column=5, pady=0, padx=2, sticky=NSEW) 

# Verifique se um ID de professor foi passado como argumento
# if len(sys.argv) > 1:
#     try:
#         professor_logado_id = int(sys.argv[1])
#     except ValueError:
#         messagebox.showerror("Erro", "ID do professor inválido.")
#         janela.destroy()
#         sys.exit()
# else:
#     messagebox.showerror("Erro", "ID do professor não fornecido.")
#     janela.destroy()
#     sys.exit()
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
            messagebox.showerror("Erro", f"Preencha todos os campos ")
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

# Abrindo A imagem
    imagem = Image.open('Icones/aluno.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)
    
    # Mostrando os valores da tabela
    mostrar_alunos()

# Procurar Aluno
def procurar():
    global imagem, imagem_string, l_imagem # Assume que essas variáveis estão definidas globalmente

    id_aluno = None # Inicializa id_aluno como None
    dados = None    # Inicializa 'dados' como None para garantir que sempre exista

    # 1. Tenta obter e converter o ID do aluno da entrada
    try:
        # Pega o texto do campo de entrada e remove espaços em branco extras
        id_input = e_procurar.get().strip() 
        if id_input: # Se o campo não estiver vazio
            id_aluno = int(id_input) # Tenta converter para inteiro
        # Se o campo estiver vazio, id_aluno permanecerá None
            
    except ValueError:
        # Se a conversão para int falhar (ex: digitou texto)
        print("Erro: ID de aluno inválido. Por favor, digite um número.")
        # id_aluno permanece None, o que fará com que o bloco 'else' final seja executado
        
    # 2. Se um ID numérico válido foi obtido, tenta buscar o aluno
    if id_aluno is not None:
        # Sua função real de busca por aluno.
        # É CRUCIAL que search_studant retorne 'None' se o aluno não for encontrado!
        dados = sistema_de_registro.search_studant(id_aluno) 

    # 3. Processa o resultado: Aluno Encontrado OU Não Encontrado / Entrada Inválida
    if dados: # Este bloco é executado APENAS SE 'dados' NÃO FOR 'None' (ou seja, aluno encontrado)
        print(f"Aluno encontrado para ID: {id_aluno}")
        
        # Limpa TODOS os campos antes de preencher com os novos dados
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        # Insere os valores nos campos.
        # ATENÇÃO: Verifique se os índices (dados[1], dados[2]...) correspondem
        # à ordem das colunas retornadas pela sua query SQL em `search_studant`!
        e_nome.insert(END, dados[1])
        e_email.insert(END, dados[2])
        e_tel.insert(END, dados[3])
        c_sexo.insert(END, dados[4])
        data_nascimento.insert(END, dados[5])
        e_endereco.insert(END, dados[6])
        c_curso.insert(END, dados[7])

        # Carrega a imagem específica do aluno
        imagem_caminho = dados[8] # Assume que dados[8] contém o caminho da imagem
        imagem_string = imagem_caminho # Atualiza a variável global 'imagem_string' se necessário

        try:
            temp_imagem = Image.open(imagem_caminho)
            temp_imagem = temp_imagem.resize((130,130))
            imagem = ImageTk.PhotoImage(temp_imagem) # Atualiza a variável global 'imagem'

            # Atualiza o label da imagem existente ou o cria se for a primeira vez
            if l_imagem:
                l_imagem.config(image=imagem)
            else:
                l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
                l_imagem.place(x=390, y=10)
            
            # Se você tiver um botão 'Trocar De Foto', atualize o texto aqui
            # Garanta que 'botao_carregar' está definido globalmente ou acessível.
            if 'botao_carregar' in globals(): # Verifica se o botão existe antes de tentar acessá-lo
                botao_carregar['text'] = 'Trocar De Foto'

        except FileNotFoundError:
            print(f"Erro: Imagem do aluno '{imagem_caminho}' não encontrada. Carregando imagem padrão.")
            # Se a imagem específica não for encontrada, o fluxo cairá no 'else' abaixo.
        except Exception as e:
            print(f"Ocorreu um erro ao carregar a imagem do aluno: {e}. Carregando imagem padrão.")
            # Mesma lógica que FileNotFoundError.
            
    else: # Este bloco é executado SE 'dados' é 'None' (aluno não encontrado) OU se 'id_aluno' era 'None' (entrada inválida/vazia)
        print("Nenhum aluno encontrado para o ID fornecido ou entrada inválida. Limpando campos e carregando imagem padrão.")
        
        # Limpa TODOS os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        # Carrega a imagem padrão (aluno.png)
        try:
            temp_imagem = Image.open('Icones/aluno.png') # Certifique-se de que o caminho está correto
            temp_imagem = temp_imagem.resize((130,130))
            imagem = ImageTk.PhotoImage(temp_imagem) # Atualiza a variável global 'imagem'

            if l_imagem: # Se o label da imagem já existe, apenas o configura
                l_imagem.config(image=imagem)
            else: # Senão, cria o label pela primeira vez
                l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
                l_imagem.place(x=390, y=10)
            
            # Atualiza o texto do botão para indicar o estado padrão
            if 'botao_carregar' in globals():
                botao_carregar['text'] = 'Carregar Foto' # Ou outro texto apropriado para o estado padrão

        except FileNotFoundError:
            print("Erro: Imagem 'Icones/aluno.png' não encontrada. Verifique o caminho.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar a imagem padrão: {e}")
            
    # Sempre limpa o campo de entrada do ID após a operação e coloca o foco de volta 
    e_procurar.focus_set()

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
data_nascimento = DateEntry(frame_details, width=11, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
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

    nova_imagem_caminho = fd.askopenfilename()

    if nova_imagem_caminho:
        imagem_string = nova_imagem_caminho 
        temp_imagem = Image.open(nova_imagem_caminho)
        temp_imagem = temp_imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(temp_imagem)
        l_imagem.config(image=imagem)
        l_imagem.image = imagem 
        botao_carregar['text'] = 'Trocar De Foto'



botao_carregar = Button(frame_details,command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)


# Criando tabelas de alunos Alunos
def mostrar_alunos():

    #
    list_header = ['id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']

    df_list= sistema_de_registro.view_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # Definindo os cabeçalhos das colunas
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    # Posicionando a Treeview e as barras de rolagem
    tree_aluno.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    # Configurando o peso das linhas e colunas do frame para que a Treeview se expanda
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", 'center', 'center', 'center', 'center', 'center']
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:   
        tree_aluno.insert('', 'end', values=item)        
        # Adicione esta linha para exibir a tabela ao iniciar o programa
    return tree_aluno

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
