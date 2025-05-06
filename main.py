import sqlite3 
from tkinter import messagebox


class SistemaDeRegistro:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.creat
