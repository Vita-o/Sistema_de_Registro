#importando dependencias do Tkinter
import tkinter as tk
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

janela.grid_columnconfigure(0, weight=1) # Peso para a primeira coluna (onde o frame_botoes está)
janela.grid_columnconfigure(1, weight=1) # Peso para a segunda coluna (onde o frame_details está)
janela.grid_columnconfigure(2, weight=1) # Peso para a terceira coluna (vazia, mas pode influenciar)
janela.grid_columnconfigure(3, weight=1) # Peso para a quarta coluna (vazia, mas pode influenciar)
janela.grid_columnconfigure(4, weight=1) # Peso para a quinta coluna (onde o frame_tabela está)
janela.grid_rowconfigure(3, weight=1) 

# ================================== Criando Frames ==================================
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=530, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=780, height=300, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky="nsew", columnspan=5)

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
        subprocess.Popen(['c:/Users/victor.barbosa/Desktop/Sistema_de_Registro/venv/Scripts/python.exe', 'telalogin.py'])


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
l_imagem.grid(row=0, column=4, rowspan=3, pady=10, padx=0, sticky=NSEW)

#================================== Criando funçoes para CRUD ==================================

def calcular_media(*args):
    try:
        nota1 = float(e_nota1.get()) if e_nota1.get() else 0.0
        nota2 = float(e_nota2.get()) if e_nota2.get() else 0.0
        nota3 = float(e_nota3.get()) if e_nota3.get() else 0.0
        nota4 = float(e_nota4.get()) if e_nota4.get() else 0.0
        media = (nota1 + nota2 + nota3 + nota4) / 4
        e_media.config(state=NORMAL)
        e_media.delete(0, tk.END)
        e_media.insert(tk.END, media)
        e_media.config(state=DISABLED)
        print(media)
    except ValueError:
        e_media.config(state=NORMAL)
        e_media.delete(0, tk.END)
        e_media.insert(tk.END, "---")
        e_media.config(state=DISABLED)

# Procurar Aluno
def procurar():
    global imagem, imagem_string, l_imagem

    e_nome.config(state='normal')
    # l_nome.config(state='normal') 

    e_faltas.config(state='normal')
    # l_faltas.config(state='normal') 

    id_aluno = None 
    dados = None    

    try:
        id_input = e_procurar.get().strip() 
        if id_input: 
            id_aluno = int(id_input)
            
    except ValueError:
        print("Erro: ID de aluno inválido. Por favor, digite um número.")
        
    if id_aluno is not None:
        dados = sistema_de_registro.search_studant(id_aluno) 

    if dados: 
        print(f"Aluno encontrado para ID: {id_aluno}")
        
        e_nome.delete(0, END)
        e_nota1.delete(0, END)
        e_nota2.delete(0, END)
        e_nota3.delete(0, END)
        e_nota4.delete(0, END)
        e_faltas.delete(0, END)
        e_media.delete(0, END) 

        e_nome.insert(END, dados[1])    
        e_nota1.insert(END, dados[10])   
        e_nota2.insert(END, dados[11])   
        e_nota3.insert(END, dados[12])   
        e_nota4.insert(END, dados[13])   
        e_faltas.insert(END, dados[9])   

        imagem_caminho = dados[8] 
        imagem_string = imagem_caminho 

        try:
            temp_imagem = Image.open(imagem_caminho)
            temp_imagem = temp_imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(temp_imagem) 

            if l_imagem:
                l_imagem.config(image=imagem)
            else:
                l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
                l_imagem.grid(row=0, column=4, rowspan=3, pady=10, padx=0, sticky=NSEW)
            

        except FileNotFoundError:
            print(f"Erro: Imagem do aluno '{imagem_caminho}' não encontrada. Carregando imagem padrão.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar a imagem do aluno: {e}. Carregando imagem padrão.")

        try:
            nota1 = float(e_nota1.get())
            nota2 = float(e_nota2.get())
            nota3 = float(e_nota3.get())
            nota4 = float(e_nota4.get())
            
            media = (nota1 + nota2 + nota3 + nota4) / 4
            e_media.insert(END, str(media))
        except ValueError:
            print("Erro ao calcular média: Notas não são números válidos.")
            e_media.delete(0, END) 
        except Exception as e:
            print(f"Erro inesperado ao calcular média: {e}")
            e_media.delete(0, END) 

    else: 
        print("Nenhum aluno encontrado para o ID fornecido ou entrada inválida. Limpando campos e carregando imagem padrão.")
        
        e_nome.delete(0, END)
        e_nota1.delete(0, END)
        e_nota2.delete(0, END)
        e_nota3.delete(0, END)
        e_nota4.delete(0, END)
        e_faltas.delete(0, END)
        e_media.delete(0, END) 

        try:
            temp_imagem = Image.open('Icones/aluno.png') 
            temp_imagem = temp_imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(temp_imagem) 

            if l_imagem:
                l_imagem.config(image=imagem)
            else:
                l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
                l_imagem.grid(row=0, column=4, rowspan=3, pady=10, padx=0, sticky=NSEW)
            

        except FileNotFoundError:
            print("Erro: Imagem 'Icones/aluno.png' não encontrada. Verifique o caminho.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar a imagem padrão: {e}")
            

    e_procurar.focus_set()

    e_nome.config(state='disabled') 
   

    e_faltas.config(state='disabled') 
   
#  Atualizar 
def atualizar():
    global imagem, imagem_string, l_imagem

    id_aluno = None 
    try:
        id_input = e_procurar.get().strip() 
        if id_input: 
            id_aluno = int(id_input)
        else:
            messagebox.showwarning('Aviso', 'Por favor, digite o ID do aluno a ser atualizado.')
            e_procurar.delete(0, END) 
            e_procurar.focus_set() 
            return 
            
    except ValueError:
        messagebox.showerror('Erro', 'ID inválido. Por favor, digite um número.')
        e_procurar.delete(0, END) 
        e_procurar.focus_set() 
        return 

    try:
        nota1 = int(e_nota1.get())
        nota2 = int(e_nota2.get())
        nota3 = int(e_nota3.get())
        nota4 = int(e_nota4.get())
    except ValueError:
        messagebox.showerror('Erro', 'As notas devem ser números inteiros válidos.')
        return 

    lista = [nota1, nota2, nota3, nota4, id_aluno]

    status_atualizacao = sistema_de_registro.notas_studante(lista)

    if status_atualizacao:
        messagebox.showinfo('Sucesso', 'Notas do aluno atualizadas com sucesso!')
        print(f"Notas do aluno com ID {id_aluno} atualizadas.")
        # procurar() 


    e_procurar.focus_set()
    
    mostrar_alunos()

    try:
        nota1 = float(e_nota1.get()) if e_nota1.get() else 0.0
        nota2 = float(e_nota2.get()) if e_nota2.get() else 0.0
        nota3 = float(e_nota3.get()) if e_nota3.get() else 0.0
        nota4 = float(e_nota4.get()) if e_nota4.get() else 0.0
        media = (nota1 + nota2 + nota3 + nota4) / 4
        e_media.config(state=NORMAL)
        e_media.delete(0, tk.END)
        e_media.insert(tk.END, media)
        e_media.config(state=DISABLED)
        print(media)
    except ValueError:
        e_media.config(state=NORMAL)
        e_media.delete(0, tk.END)
        e_media.insert(tk.END, "---")
        e_media.config(state=DISABLED)

    # Mostrando os valores da tabela
    mostrar_alunos()

# ================================== Campos de Entrada ==================================
l_nome = Label(frame_details, text="Nome Do Aluno", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=0, padx=20, sticky=NSEW)
e_nome = Entry(frame_details, width=60, justify='left', relief='solid')
e_nome.grid(row=0, column=0, columnspan=2, pady=15, padx=20)

e_nome.config(state=DISABLED)
l_nome.config(state=DISABLED)

l_nota1 = Label(frame_details, text="Nota1 *",justify='center', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nota1.grid(row=1, column=0, pady=0, padx=25, sticky=NSEW)
e_nota1 = Entry(frame_details, width=20, justify='center', relief='solid')
e_nota1.grid(row=1, column=0, pady=15, padx=20, sticky='w')

l_nota2 = Label(frame_details, text="Nota2 *",justify='center', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nota2.grid(row=1, column=1, pady=0, padx=25, sticky=NSEW)
e_nota2 = Entry(frame_details, width=20, justify='center', relief='solid')
e_nota2.grid(row=1, column=1, pady=15, padx=20, sticky='w')

l_nota3 = Label(frame_details, text="Nota3 *",justify='center', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nota3.grid(row=2, column=0, pady=0, padx=25, sticky=NSEW)
e_nota3 = Entry(frame_details, width=20, justify='center', relief='solid')
e_nota3.grid(row=2, column=0, pady=15, padx=20, sticky='w')

l_nota4 = Label(frame_details, text="Nota4 *",justify='center', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nota4.grid(row=2, column=1, pady=0, padx=25, sticky=NSEW)
e_nota4 = Entry(frame_details, width=20, justify='center', relief='solid')
e_nota4.grid(row=2, column=1, pady=15, padx=20, sticky='w')


# Criando Cursos

l_media = Label(frame_details, text="MEDIA DO ALUNO", anchor=CENTER, font=('Ivy 10'), bg=co1, fg=co4)
l_media.grid(row=4, column=0,   columnspan=2, pady=0, padx=0, sticky=NSEW)
e_media = Entry(frame_details, width=40, justify='center', relief='solid')
e_media.grid(row=5, column=0, columnspan=2, pady=0, padx=0)

e_media.config(state=DISABLED)
l_media.config(state=DISABLED)


#================================== Função para escolher imagem ==================================

l_faltas = Label(frame_details, text="faltas *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_faltas.grid(row=5, column=4, pady=0, padx=0, sticky=NSEW)
e_faltas = Entry(frame_details, width=5, justify='left', relief='solid')
e_faltas.grid(row=5, column=4, pady=0, padx=0)

e_faltas.config(state=DISABLED)
l_faltas.config(state=DISABLED)

tree_alunos = None  # Variável global para a Treeview
estados_checkboxes = {} # Dicionário para guardar o estado dos checkboxes

# ================================== Pegando a Materia do professor ==================================

def obter_materia_professor(professor_id):
    """Obtém a matéria do professor logado."""
    dados_professor = sistema_de_usuario.search_usuario(professor_id)
    if dados_professor and len(dados_professor) > 8: # Verifica se a matéria existe
        return dados_professor[8] # A matéria está na nona posição (índice 8)
    return None




# ======================= Mosrando alunos que tem a memsa materia do professor =======================

def mostrar_alunos():
    global tree_alunos, estados_checkboxes, materia_professor, professor_logado_id

    materia_professor = obter_materia_professor(professor_logado_id)

    if not materia_professor:
        messagebox.showerror("Erro", "Não foi possível obter a matéria do professor.")
        return

    list_header = ['ID', 'Nome'] + [f'Dia {i+1}' for i in range(25)]
    alunos_da_materia = sistema_de_registro.get_alunos_por_materia(materia_professor)
    estados_checkboxes = {}

    if tree_alunos:
        tree_alunos.destroy()


    tree_alunos = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # Definindo os cabeçalhos e impedindo o esticamento das colunas (stretch=NO)
    tree_alunos.heading('ID', text='ID', anchor='center')
    tree_alunos.column('ID', width=50, anchor='center', stretch=NO)
    tree_alunos.heading('Nome', text='Nome', anchor='nw')
    tree_alunos.column('Nome', width=150, anchor='nw', stretch=NO)
    for i in range(25):
        tree_alunos.heading(f'Dia {i+1}', text='', anchor='center')
        tree_alunos.column(f'Dia {i+1}', width=30, anchor='center', stretch=NO)

    # Adicionando barras de rolagem
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_alunos.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_alunos.xview)
    tree_alunos.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_alunos.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

# Inserir dados na tabela e restaurar estados
    for aluno in alunos_da_materia:
        aluno_id = aluno[0]
        nome_aluno = aluno[1]
        total_faltas = aluno[2] if len(aluno) > 2 else 0 # Pega o valor de 'faltas' (índice 9)
        estados_aluno = [False] * 25 # Inicializa todos como presente

        # Marca os primeiros 'total_faltas' dias como falta
        for i in range(total_faltas):
            if i < 25:
                estados_aluno[i] = True

        values = [aluno_id, nome_aluno] + ['[X]' if estado else '[ ]' for estado in estados_aluno]
        tree_alunos.insert('', 'end', values=values)
        estados_checkboxes[aluno_id] = list(estados_aluno)

    tree_alunos.bind('<Button-1>', on_treeview_click)
    return tree_alunos
# ================================== Marcando caixas de faltas ==================================

def on_treeview_click(event):
    global tree_alunos, estados_checkboxes, sistema_de_registro
    item_id = tree_alunos.identify_row(event.y)
    column_id = tree_alunos.identify_column(event.x)

    if item_id and column_id not in ('#0', '#1'):
        col_index = int(column_id[1:]) - 2
        aluno_id_str = tree_alunos.item(item_id, 'values')[0]
        try:
            aluno_id = int(aluno_id_str)

            if aluno_id in estados_checkboxes:
                current_state = estados_checkboxes[aluno_id][col_index]
                estados_checkboxes[aluno_id][col_index] = not current_state
                novo_marcador = '[X]' if estados_checkboxes[aluno_id][col_index] else '[ ]'
                tree_alunos.set(item_id, column_id, novo_marcador)

                # Calcular o total de faltas com base nos checkboxes
                total_faltas = sum(1 for estado in estados_checkboxes[aluno_id] if estado)
                sistema_de_registro.atualizar_faltas(aluno_id, total_faltas)

        except ValueError:
            print(f"Erro ao converter aluno_id para inteiro: {aluno_id_str}")
#================================== Procurar Aluno ==================================
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar Aluno [Entra ID] *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_alterar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_alterar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

botao_alterar = Button(frame_procurar, command=calcular_media, text='MEDIA', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_alterar.grid(row=2, column=1, pady=10, padx=0, sticky=NSEW)


#================================== Botoes =================================

app_img_atualizar = Image.open('Icones/update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text=' Atualizar ', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)



# Linha Separatoria
l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co0, fg=co1)
l_linha.place(x=240, y=15)

# Chamando a função para criar e exibir a tabela
mostrar_alunos()

janela.mainloop()