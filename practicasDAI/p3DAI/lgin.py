 #!/usr/bin/python
 # -*- coding: UTF-8 -*-
from flask import Flask, session, redirect, url_for, escape, request, make_response
from flask import render_template
import re
from RegistrationForm import RegistrationForm
from persona import Persona
from pymongo import MongoClient
from wtforms import Form, BooleanField, TextField, PasswordField, validators, SelectField, DateField, TextAreaField, RadioField, ValidationError

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


#session = session.get(initializer={'iniciado':False})
#session.visitadas2=session.get()


@app.route('/')
def index():
    if 'username' in session:
        print "El usuario en sesion"

    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mongoClient = MongoClient('localhost',27017)
        db = mongoClient.Individuos
        collection = db.individuo
        print "Comprueba persona"
        person = collection.find({"nombre":request.form['username'],"password":request.form['password']})
        if not person.count()==0:
            print "La ha encontrado"
            session['username'] = request.form['username']
            print session['username']
        return redirect(url_for('index'))

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
        mongoClient = MongoClient('localhost',27017)
        db = mongoClient.Individuos
        collection = db.individuo
        persona = Persona(form.username.data,form.second_name.data,form.VISA.data,form.email.data,form.birthday.data,form.birthmoth.data,form.birthyear.data,form.password.data)
        collection.insert(persona.toDBCollection())
        person = collection.find_one({"nombre":form.username.data,"password":form.password.data})
        session['username'] = person['nombre']
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    print "hooolalal"
    req = request.form
    form = RegistrationForm(req)


    if 'username' in session:
        mongoClient = MongoClient('localhost',27017)
        db = mongoClient.Individuos
        collection = db.individuo
        person = collection.find_one({"nombre":session['username']})
    
        if request.method == 'POST':
            person['nombre']=form.username.data
            person['apellidos']=form.second_name.data
            person['correo']=form.email.data
            person['dia']=form.birthday.data
            person['mes']=form.birthday.data
            person['year']=form.birthmoth.data
            person['VISA']=form.VISA.data
            person['password']=form.password.data
            collection.save(person)
            return redirect(url_for('index'))

        else:
            form.username.data=person['nombre']
            form.second_name.data=person['apellidos']
            form.email.data=person['correo']
            form.birthday.data=person['dia']
            form.birthmoth.data=person['mes']
            form.birthyear.data=person['year']
            form.VISA.data=person['VISA']
            form.password.data=person['password']

    return render_template('update.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



if __name__ == '__main__':
    app.run(debug=True)
