# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask.ext.wtf import Form
from wtforms.validators import Required
from wtforms import TextField, TextAreaField, DateTimeField, PasswordField

class ExampleForm(Form):
	title = TextField(u'標題', validators = [Required()])
	content = TextAreaField(u'內容')
	date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField(u'帳號', validators = [Required()])
	password = PasswordField(u'密碼', validators = [Required()])
