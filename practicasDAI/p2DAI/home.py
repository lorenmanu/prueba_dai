import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
	username=TextField('Nombre de usuario', [validators.Length(min=4,max=25)])
	email = TextField('Direccion email', [validators.Length(min=4,max=25)])
	password = PasswordField('Contrasenia', [validators.Required(),validators.EqualTo('confirm',message='lA CONTRASEniaA DEBE COINCIDIR CON LA REPETICION')])

	confirm = PasswordField('Repite la contrasenia')
	accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('base.html')

@app.route('/user/<username>')
def mostrarPerfilUsuario(username=None,par1=None,par2=None):
	parametro1 = request.args.get('par1')  
	parametro2 = request.args.get('par2')

	return render_template('perfil.html', usuario=username,par1=parametro1,par2=parametro2)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('perfil.html', usuario=username,par1=parametro1,par2=parametro2)

@app.route('/register',methods=['GET','POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		return ('Gracias')

	return render_template('register.html',form=form)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0')
