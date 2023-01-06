from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser
from controller.auth import validateLogin
import calendar


###
### Home route
### Checks if the user is logged in and then list the calendar, otherwise send it back to login screen

@app.route('/')
def home():
    if session:
        if (session['user_logged_in'] == True):

            cal = calendar.Calendar(firstweekday=6)
            DIAS_DA_SEMANA = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
            calDays = cal.monthdayscalendar(2022, 12)
            user_info = [session['ID'],session['user']]

            return render_template('calendar.html', calDays=calDays, aux=0, DIAS_DA_SEMANA=DIAS_DA_SEMANA, user_info=user_info)
        else:
            return redirect(url_for('login'))
    else:
        return redirect('/login')


@app.route('/new_event/', methods=['POST'])
def new_event():
    pass

### End of Home route


###
### Login and Authenticate routes
###
@app.route('/login/')
def login():
    return render_template('login.html', titulo = 'User login')

@app.route('/autenticate', methods=['POST',])
def autenticate():
    autenticated, user_auth = validateLogin(request.form['user_name'], request.form['password'])
    
    if autenticated:
        session['user_logged_in'] = True
        session['user'] = user_auth.user_name
        session['ID'] = user_auth.id
        
        flash('Successfully logged in')

        return redirect(url_for("home"))
    else:
        flash('Invalid credentials')
        return redirect(url_for("login"))

@app.route('/logout/')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

#### End of Login routes

###
### User manupulation
###

### List all users 
@app.get('/users/')
def users_list():
    users_list = listUsers()
    print(users_list)
    return render_template('list_users.html', title = 'User list', users_list=users_list)

### Create a new user on the database:
@app.post('/users/')
def new_user():
    
    print(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
    createUser(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
    
    flash(f"User {request.form['user_name']} created.")
    
    return redirect(url_for("home"))

### List a user by his ID
@app.get('/users/<id>/')
def listUserByID(id):
    users_list = listUsers(id)
    print(users_list)
    return render_template('list_single_user.html', title = 'User list', user=users_list)

### List a user by his ID
@app.get('/users/edit/<id>/')
def editUserForm(id):
    users_list = listUsers(id)
    print(users_list)
    return render_template('edit_user.html', title = 'Edit user: ' + users_list.name, user=users_list)

### Edit a user by his ID
@app.patch('/users/<id>/')
def editUserByID(id):

    isAdmin = False
    if request.form['admin'] == "True":
        isAdmin = True
    updateUser(id, request.form['name'], isAdmin )
    return "WOHO"

### Deletes a user by his ID
@app.delete('/users/<id>/')
def deleteUserByID(id):
    pass

### Form to add new users
@app.route('/users/new_user')
def new_user_form():
    if session:
        if (session['user_logged_in'] == True):

            user_info = [session['ID'],session['user']]

            return render_template('form_new_user.html', user_info=user_info)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

    
### End of User routes