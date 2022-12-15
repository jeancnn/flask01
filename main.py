from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import *


app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_pyfile('config.py')


@app.route('/')
def inicio():
    if session:
        if (session['logged_in'] == True):
            return render_template('index.html', pessoas=pessoas, title='Home')
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

    if app.secret_key == request.form['senha']:

        session['logged_in'] = True
        flash('DEU BOA')
        return redirect(url_for('inicio'))
    
    else:
        flash('senha invalida')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('VOCE FOi DESCONECTADO')
    return redirect(url_for('login'))



app.run(debug=True)