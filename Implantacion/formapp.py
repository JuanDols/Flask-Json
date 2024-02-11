from flask import Flask, render_template, session,redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields.core import RadioField, SelectField
from wtforms.fields.simple import SubmitField, StringField, BooleanField, TextAreaField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asix2324'
from forms import InfoForm,SecondInfoForm,ThirdInfoForm,FourthInfoForm,DynamicForm,ValidatedForm

combo_extra_options = {
    '1': 'first',
    '2': 'second'
}

#@app.route('/', methods=['GET', 'POST'])
def firstform():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():  # torna true si l'usuari fa clic al submit i tot ok
        breed = form.breed.data  # conte el text que ha escrit l'usuari
        print(breed)
        form.breed.data = ''
    return render_template('firstformtest.html', form=form, breed=breed)

#@app.route('/', methods=['GET', 'POST'])
def secondForm():
    form = SecondInfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data #tractamos session como un diccionario
        session['neutered']= form.neutered.data
        session['mood']= form.mood.data
        session['favourite_food']=form.favourite_food.data
        session['comments'] = form.comments.data

        return redirect(url_for('secondFormThankyou'))


    return render_template('secondformtest.html', form=form)

#@app.route('/form/second/thankyou', methods=['POST','GET'])
def secondFormThankyou():
    return render_template('secondformthankyou.html')

#@app.route('/',methods = ['POST','GET'])
def thirdForm():
    form = ThirdInfoForm()
    if form.validate_on_submit():
        flash('You just click the button!!')
        #return redirect(url_for('thirdFormThankyou'))

    return render_template('thirdformtest.html', form=form)


#@app.route('/',methods = ['POST','GET'])
def fourthForm():
    form= FourthInfoForm()
    #sobreescribimos todas las opciones de combobox de una
    form.dynamic_choice.choices = [(0,'choose'), (1,'Español'), (2,'English')]
    if form.validate_on_submit():
        choice_value = form.dynamic_choice.data #0, 1 o 2
        if choice_value != 0:
            choice_text = form.dynamic_choice.choices[choice_value][1]
            session['dynamic_choice'] = choice_text
            return render_template('fourthformthankyou.html')
    return render_template('fourthformtest.html', form=form)

#@app.route('/',methods = ['POST','GET'])
def dynamicForm():
    form = DynamicForm()
    #añadimos opciones dinamicas, normalmente desde un resultado de query
    for option in combo_extra_options.items():
        form.combo_box.choices.append(option)
    #no validamos esto solo es para mostrar como añadir opciones
    return render_template('dynamicformtest.html', form=form)

@app.route('/',methods = ['GET','POST'])
def validatedForm():
    form = ValidatedForm()
    if form.validate_on_submit():
        flash('form validated correctly')
        #tendria que hacer un redirect o render template de paghina siguiente
    return render_template('validatedFormtest.html',form= form)

if __name__ == '_main_':
    app.run()