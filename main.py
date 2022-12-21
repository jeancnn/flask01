from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from views import *
from controller import auth
import calendar


app = Flask(__name__)
#db = SQLAlchemy(app)

app.config.from_pyfile('config.py')


@app.route('/')
def inicio():
    if session:
        if (session['usuario_logado'] == True):

            cal = calendar.Calendar(firstweekday=6)
            DIAS_DA_SEMANA = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")
            calDays = cal.monthdayscalendar(2022, 12)

            return render_template('calendario.html', calDays=calDays, aux=0, DIAS_DA_SEMANA=DIAS_DA_SEMANA)
        else:
            return redirect(url_for('login'))
    else:
        return redirect('/login')

@app.route('/novo')
def novo():
    if session:
        if (session['logged_in'] == True):
                return render_template('cadastro.html', pessoas=pessoas, title='Cadastro')
    else:    
        return redirect(url_for('login'))
    


@app.route('/cadastro', methods=['POST'])
def cadastrar():
    pessoas.append(Pessoa(request.form['nome'], request.form['idade']))
    return redirect(url_for('inicio'))


@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login Usuario')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    autenticado = auth.validaLogin(request.form['usuario'], request.form['senha'])
    if autenticado:
        session['usuario_logado'] = True
        
        flash('Logado com sucesso')

        return redirect(url_for("inicio"))
        
        
        

@app.route('/logout')
def logout():
    session.clear()
    flash('VOCE FOi DESCONECTADO')
    return redirect(url_for('login'))



app.run(debug=True)