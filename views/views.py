from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listAllUsers
import calendar

@app.route('/')
def home():
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

@app.route('/new_user')
def new_user():
    if session:
        if (session['logged_in'] == True):
                return render_template('cadastro.html', pessoas=pessoas, title='Cadastro')
    else:    
        return redirect(url_for('login'))
    


@app.route('/new_event', methods=['POST'])
def new_event():
    pass

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'User login')

@app.route('/autenticate', methods=['POST',])
def autenticar():
    autenticado = auth.validaLogin(request.form['usuario'], request.form['senha'])
    if autenticado:
        session['usuario_logado'] = True
        
        flash('Successfully logged in')

        return redirect(url_for("home"))
        
@app.route('/logout')
def logout():
    session.clear()
    flash('VOCE FOi DESCONECTADO')
    return redirect(url_for('login'))


@app.route('/user_list')
def user_list():
    pessoas = listAllUsers()
    print(pessoas)
    return render_template('list_all.html', titulo = 'User list', pessoas=pessoas)