efrom wtforms.validators import InputRequired, NoneOf, Regexp, ValidationError

import app
from flask import Flask, render_template, session,redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields.core import RadioField, SelectField, StringField
from wtforms.fields.simple import SubmitField, BooleanField, TextAreaField


class InfoForm(FlaskForm):
    breed = StringField('What breed is your pet?')
    submit = SubmitField('Submit')


class SecondInfoForm(FlaskForm):
    breed = StringField('What breed is your')
    neutered = BooleanField('Has the pet been neutered?')  # checkbox
    mood = RadioField(
        'How is your pet feeling',
        choices=[('mood1', 'happy'), ('mood2', 'sad'), ('mood3', 'neutral')]
    )
    favourite_food = SelectField('What favourite food?',
                                 choices=[('food1', 'chiken'), ('food2', 'tuna'), ('food3', 'beef')])
    comments = TextAreaField('')
    submit = SubmitField('Submit')


class ThirdInfoForm(FlaskForm):
    submit = SubmitField('Click me!')


class FourthInfoForm(FlaskForm):
    dynamic_choice = SelectField('Pick your choice', coerce =int)
    submit = SubmitField('Submit')


class DynamicForm(FlaskForm):
    combo_box = SelectField('Dynamic ComboBox',
                            choices=[('', 'choose one')])
    submit = SubmitField('Submit')

def validate_DNI(form, field): #funcion custom necesira de formulario i campo a validar
    char = 'TRWAGMYFPDXBNJZSQVHLCKE'
    dni = field.data #00000000T 00000001R 0000000W
    number = int(dni[0:8]) #00000000 00000001 00000002
    letter = dni[8] #T,R,W
    if letter != char[number % 23]:#letra no coincide
        raise ValidationError('Wrong DNI')#lanzamos error de validacion. Si esto esta okay, no hacemos nada

class ValidatedForm(FlaskForm):

    text = StringField('String to test Valid',
                       validators=[
                           InputRequired(message = 'Field cannot be empty'),
                           NoneOf(values=['forbiden_value','abc'],
                                  message='Value forbidden')
                       ])
    regex = StringField('Regex to test validation',
                        validators=[Regexp('^A.*$')]) #Comienza por A

    custom = StringField('String with custom validator',
                         validators = [validate_DNI])

    submit = SubmitField('Click to validate')