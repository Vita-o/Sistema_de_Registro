import sqlite3 
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execulte('''CREATE TABLE IF NOT EXISTS estudantes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        tel TEXT NOT NULL,
                        sexo TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        endereco TEXT NULL,
                        curso TEXT NOT NULL,
                        picture TEXT NOT NULL)''')
        
    def register_studant(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
                       (estudantes))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo()