 #!/usr/bin/python
 # -*- coding: UTF-8 -*-
from flask import Flask, flash, session, redirect, url_for, escape, request, make_response
from flask import render_template
import re
from Update import RegistrationFormUpdate
from RegistrationForm import RegistrationForm
from persona import Persona
from wtforms import Form, BooleanField, TextField, PasswordField, validators, SelectField, DateField, TextAreaField, RadioField, ValidationError
import dbm #Modulo para base de datos dbm

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

db=dbm.open('datos.dat','c')

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
         if db.has_key(request.form['username']):
            nuevo=db[request.form['username']].split(',')
            if nuevo[8] == request.form['password']:
                session['username'] = request.form['username']
                session['historial'] = []
            else:
                flash('Password incorrect','login')
         else:
            flash('Usuario inexistente','login')

    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))

    req = request.form
    form = RegistrationForm(req)

    if request.method == 'POST' and form.validate():
        db[form.username.data] = form.username.data +","+ form.second_name.data +","+ form.email.data +","+ form.birthday.data+","+form.birthmoth.data+","+form.birthyear.data+","+ form.pay.data+","+ form.VISA.data +"," + form.password.data
        nuevo=db[form.username.data].split(',')
        session['username']=nuevo[0]
        session['historial'] = []
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    req = request.form
    form = RegistrationFormUpdate(req)

    if request.method == 'POST':
        if form.validate():
            print "Entra AQUI3"
            db[session['username']] = form.username.data +","+ form.second_name.data +","+ form.email.data +","+ form.birthday.data+","+form.birthmoth.data+","+form.birthyear.data+","+ form.pay.data+","+ form.VISA.data +"," + form.password.data
            nuevo=db[session['username']].split(',')
            print nuevo[0]
            return redirect(url_for('index'))

    if 'username' in session:
        print "Entra AQUI"
        nuevo=db[session['username']].split(',')
        form.username.data=nuevo[0]
        form.second_name.data=nuevo[1]
        form.email.data=nuevo[2]
        form.birthday.data=nuevo[3]
        form.birthmoth.data=nuevo[4]
        form.birthyear.data=nuevo[5]
        form.pay.data=nuevo[6]
        form.VISA.data=nuevo[7]
        form.password.data=nuevo[8]

    return render_template('update.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('historial')
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.before_request
def historial():
    if 'historial' in session:
        session['historial'].append(request.url)
        if len(session['historial']) > 3:
            session['historial'].pop(0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
