import hashlib
import sqlite3


try:
    conn = sqlite3.connect('agenda.db', check_same_thread=False)
except:
    print("Erro ao connectar com o banco")
    conn = False

if conn:
    print("Ainda funfando")
    
cursor = conn.cursor()

def validaLogin(usuario, senha):

    sql_select_query = """select * FROM usuario WHERE username = ?"""
    cursor.execute(sql_select_query, (usuario,))
    records = cursor.fetchall()

    print(records)
    
    if records == []:
        print("Erro")
        return "Erro"

    #print(records[0][4])
    
    if records[0][4] == hashlib.sha256(senha.encode('utf-8')).hexdigest():
        print("Senha correta")
        return True
    
    # if session:
    #     if (session['logged_in'] == True):
    #         return redirect(url_for('inicio'))
            

    # elif (user_db.senha == hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest()):
    #     session['logged_in'] = True
    #     return redirect(url_for('inicio'))

    # else:
    #     flash('senha invalida')
    #     return redirect(url_for('login'))

def listaPessoas():
    sql_select_query = """select * FROM usuario"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records