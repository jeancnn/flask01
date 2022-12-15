import psycopg2
import hashlib


try:
    conn = psycopg2.connect(host = "localhost", port = "5435", database = "postgres", user="teste", password = "123456")
    print("BOOOM!!")
except:
    print("Erro ao conectar")
    conn = False


if conn:
    print("Ainda funfando")
    
    cursor = conn.cursor()
    
    # cursor.execute("CREATE TABLE login_access ( id serial PRIMARY KEY, name VARCHAR(50) NOT NULL, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(260) NOT NULL);")
    
    # cursor.execute("CREATE TABLE games_list ( id serial PRIMARY KEY, game VARCHAR(50), genre VARCHAR(50), platform VARCHAR(50), completed BOOLEAN);")
    
    
    # v1 = input("Nome: ")
    # v2 = input("Username: ")
    # v3 = hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest()
    
    # cursor.execute("INSERT INTO login_access (name, username, password) VALUES(%s, %s, %s)", (v1, v2, v3))
    
    cursor.execute("SELECT * FROM login_access;")
    
    teste = cursor.fetchall()
    
    if teste[0][3] == hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest():
        print("Eita porra!")
    
    print(teste[0][3])


    conn.commit()
    cursor.close()
    conn.close()


