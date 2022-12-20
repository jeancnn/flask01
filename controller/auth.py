import psycopg2
import hashlib
from flask import render_template, request, redirect, session, flash, url_for

def autenticar(session, user, password):
    try:
        conn = psycopg2.connect(host = "localhost", port = "5435", database = "postgres", user="teste", password = "123456")
        print("BOOOM!!")
    except:
        print("Erro ao conectar")
        conn = False


    if conn:

        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM login_access;")
    
        user_db = User.query.filter_by(user=user).first()
        
        if session:
            if (session['logged_in'] == True):
                return redirect(url_for('inicio'))
                

        elif (user_db.senha == hashlib.sha256(input("Senha: ").encode('utf-8')).hexdigest()):
            session['logged_in'] = True
            return redirect(url_for('inicio'))

        else:
            flash('senha invalida')
            return redirect(url_for('login'))
