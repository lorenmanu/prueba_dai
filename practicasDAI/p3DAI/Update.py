from wtforms import Form, BooleanField, TextField, PasswordField, validators, SelectField, DateField, TextAreaField, RadioField, ValidationError
import re


class RegistrationFormUpdate(Form):
    def IdentificarCorreos(correo):
        match = bool(re.match('(\w+)@((\w+)\.)+(\w+)',correo))
        return match

    #Identificar numeros de tarjeta de credito validos separados por espacio o '-'
    def IdentificarTarjetasDeCredito(form, field):
        match = bool(re.match('(\d{4}( |-)){3}(\d{4})', field.data))
        if match == False:
            raise ValidationError('VISA number not valid, please insert with the format XXXX-XXXX-XXXX-XXXX')

    days = []
    for i in range(1,32):
        a = ("\'"+str(i)+"\'",i)
        days.append(a)

    month = []
    for i in range(1,13):
        a = ("\'"+str(i)+"\'",i)
        month.append(a)

    year = []
    for i in range(1900,2017):
        a = ("\'"+str(i)+"\'",i)
        year.append(a)

    username = TextField('',[ validators.InputRequired(),validators.Length(min=4, max=25)])
    second_name= TextField( '',[validators.Length(min=4, max=50),validators.InputRequired()])
    email = TextField('')
    pay = RadioField('',choices = [('VISA','VISA'),('COD','COD')])
    VISA= TextField('', [validators.Length(min=4, max=25),validators.InputRequired(), IdentificarTarjetasDeCredito])
    birthday  = SelectField('Day: ', choices=days)
    birthmoth = SelectField('Month: ', choices=month)
    birthyear = SelectField('Year: ', choices=year)
    adress = TextAreaField('',[validators.InputRequired()])
    password = PasswordField('', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contrasenia debe coincidir con la repeticion'),validators.InputRequired(),
        validators.Length(min=7)])
    confirm = PasswordField('')
