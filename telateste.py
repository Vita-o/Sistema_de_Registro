# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

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

frame_loging = Frame(janela, width=300, height=150, bg=co1, relief=SOLID)
frame_loging.grid(row=3, column=1, pady=10, padx=0, sticky=NSEW)











janela.mainloop()