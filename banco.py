import psycopg2
import hashlib
import sqlite3


try:
    conn = sqlite3.connect('agenda.db')
except:
    print("Erro ao connectar com o banco")
    conn = False

if conn:
    print("Ainda funfando")
    
    cursor = conn.cursor()
    
    # cursor.execute('CREATE TABLE usuario (id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, nome VARCHAR(50)  NOT NULL, admin bool NOT NULL, senha VARCHAR(256) NOT NULL);')
    # print('Sua tabela USUARIO foi criada!')
    
    # cursor.execute('CREATE TABLE evento (id serial PRIMARY KEY, id_usuario int NOT NULL, data_evento date NOT NULL, titulo VARCHAR(50) NOT NULL, descricao VARCHAR(200)NOT NULL, publico bool NOT NULL, ativo bool NOT NULL, FOREIGN KEY(id_usuario) REFERENCES usuario(id));')
    # print('Sua tabela EVENTO foi criada!')


    
    v1 = input("UserName: ")
    v2 = input("Nome: ")
    v3 = hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest()
    v4 = True
    
    sqlite_insert_with_param = """INSERT INTO usuario (username, nome, admin, senha) VALUES (?, ?, ?, ?);"""
    sql_dados = (v1, v2, v4, v3)
    
    
    cursor.execute(sqlite_insert_with_param, sql_dados)
    
    cursor.execute("SELECT * FROM usuario;")
    
    teste = cursor.fetchall()
    
    # if teste[0][3] == hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest():
    #    print("Eita porra!")
    
    print(teste)


    conn.commit()
    cursor.close()
    conn.close()


