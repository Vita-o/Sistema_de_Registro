import sqlite3 
from tkinter import messagebox

class SistemaDeUsuarios:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.c = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        sobrenome TEXT NOT NUL
                        email TEXT NOT NULL,
                        tel TEXT NOT NULL,
                        sexo TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        cargo TEXT NOT NULL,
                        materia TEXT,
                        picture TEXT NOT NULL,
                        senha TEXT NOT NULL)''')
        
    def register_studant(self, usuarios):
        self.c.execute("INSERT INTO usuarios(nome, sobrenome, email, tel, sexo, data_nascimento, cargo, materia,senha) VALUES (?,?,?,?,?,?,?,?)",
                       (usuarios))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro feito com sucesso!!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM usuarios")    
        dados = self.c.fetchall()

        return dados
        # for i in dados:
        #     print(f'id:{i[0]} Nome: sobrenome, {i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_studant(self, id):
        self.c.execute("SELECT * FROM usuarios WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_student(self, novo_valores):
        query = "UPDATE usuarios SET nome=?, sobrenome=?, email=?, tel=?, sexo=?, data_nascimento=?, cargo=?, materia=?, senha=? WHERE id=?"
        self.c.execute(query,novo_valores)
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Usuario com o ID:{novo_valores[8]} foi atualizado!!')
        

    def delet_student(self, id):
        self.c.execute("DELETE FROM usuarios WHERE id=?", (id))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Usuario com o ID:{id} foi Deletado!!')

# Criando uma instancia do sistema do registro
sistema_de_usuario = SistemaDeUsuarios()   




