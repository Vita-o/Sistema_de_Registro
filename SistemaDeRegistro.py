import sqlite3 
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                tel TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NULL,
                                curso TEXT NOT NULL,
                                picture TEXT NOT NULL,
                                faltas INTEGER NOT NULL DEFAULT 0
                                )''')
        
    def register_studant(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
                       (estudantes))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro feito com sucesso!!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")    
        dados = self.c.fetchall()

        return dados
        # for i in dados:
        #     print(f'id:{i[0]} Nome: {i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_studant(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_student(self, novo_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query,novo_valores)
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com o ID:{novo_valores[8]} foi atualizado!!')
        

    def delet_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # mostando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com o ID:{id} foi Deletado!!')


    def get_alunos_por_materia(self, materia_professor):
        """
        Retorna os alunos que estão cursando a matéria do professor.
        Args:
            materia_professor (str): A matéria do professor.
        Returns:
            list: Uma lista de tuplas, onde cada tupla contém (id, nome) dos alunos.
        """
        self.c.execute("SELECT id, nome FROM estudantes WHERE curso=?", (materia_professor,))
        alunos = self.c.fetchall()
        return alunos

    def atualizar_faltas(self, id_aluno, faltas):
        """Atualiza o número de faltas de um aluno."""
        self.c.execute("UPDATE estudantes SET faltas=? WHERE id=?", (faltas, id_aluno))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Faltas do aluno com ID {id_aluno} atualizadas para {faltas}.")

 


# Criando uma instancia do sistema do registro
sistema_de_registro = SistemaDeRegistro()

# Informacoes
# estudante = ('Maria', 'Maria@gmail.com', '4321', 'F', '01/08/2005', 'Brasil,Sergipe', 'Administração', 'imagem.png')
# sistema_de_registro.register_studant(estudante)

# Ver Estudantes
# todos_alunos = sistema_de_registro.view_all_students()

# procurar aluno
# aluno = sistema_de_registro.search_studant(3)

# Atualizar Aluno
# estudante = ('Maria', 'Maria@gmail.com', '4444', 'F', '01/08/2005', 'Brasil,Sergipe', 'Administração', 'imagem.png', 3)
# aluno = sistema_de_registro.update_student(estudante)

# Dletar Estudante
# sistema_de_registro.delet_student(2)

