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
                        email TEXT NOT NULL,
                        tel TEXT NOT NULL,
                        sexo TEXT NOT NULL,
                        cargo TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        materia TEXT,
                        senha TEXT NOT NULL,
                        caixa TEXT NOT NULL,                 
                        picture TEXT NOT NULL)''')
        
    def register_usuario(self, usuarios):
        self.c.execute("INSERT INTO usuarios(nome, email, tel, sexo, cargo, data_nascimento, endereco, materia, senha, caixa, picture) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                       (usuarios))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro feito com sucesso!!')

    def view_all_usuario(self):
        self.c.execute("SELECT id, nome, cargo, tel, sexo, data_nascimento, endereco, materia FROM usuarios")    
        dados = self.c.fetchall()

        return dados
        # for i in dados:
        #     print(f'id:{i[0]} Nome, {i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Cargo: {i[5]} | Data de nascimento: {i[6]} | endereco: {i[7]} | materia: {i[8]} | Senha: {i[9]} | Imagem: {i[10]}')

    def search_usuario(self, id):
        self.c.execute("SELECT * FROM usuarios WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_usuario(self, novo_valores):
        query = "UPDATE usuarios SET nome=?, email=?, tel=?, sexo=?, cargo=?, data_nascimento=?, endereco=?, materia=?, senha=?, caixa=?, picture=? WHERE id=?"
        self.c.execute(query,novo_valores)
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Usuario: {novo_valores[0]} com o ID:{novo_valores[11]} foi atualizado!!')
        

    def delet_usuario(self, id):
        self.c.execute("DELETE FROM usuarios WHERE id=?", (id))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Usuario com o ID:{id} foi Deletado!!')

    def confirmar_usuario(self, nome_usuario):
        self.c.execute("SELECT nome, senha, caixa, cargo FROM usuarios WHERE nome = ?", (nome_usuario,))
        usuario_confirmar = self.c.fetchone()
        return usuario_confirmar

    def atualizar_senha(self, nome_usuario, nova_senha):
        self.c.execute("UPDATE usuarios SET senha = ?, caixa = 0 WHERE nome = ?", (nova_senha, nome_usuario,))
        messagebox.showinfo("SUCESSO","Senha Atuazada com Sucesso!!")
        self.conn.commit()

    def get_id_por_nome(self, nome):
        self.c.execute("SELECT id FROM usuarios WHERE nome = ?", (nome,))
        resultado = self.c.fetchone()
        if resultado:
            return resultado[0]
        return None

# Criando uma instancia do sistema do registro
sistema_de_usuario = SistemaDeUsuarios()   


# Ver usuarios
# todos_alunos = sistema_de_usuario.view_all_students()


