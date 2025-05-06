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
        messagebox.showinfo('Sucesso', 'Registro feito com sucesso!!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")    
        dados = self.c.fetchall()

        for i in dados:
            print(f'id:{i[0]} Nome: {i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_studant(self, id):
        self.c.execute()