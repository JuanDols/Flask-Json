from flask import Flask, render_template

app = Flask(__name__)

'''
@app.route('/')
@app.route('/index') #podem afegir mes d'una ruta a la funció
def hello_world():  # put application's code here
    return 'Hola Jaime!'
'''
'''
@app.route('/index')
def index():
    #1.Tractar parametros
    #2.consultar modelo
    user = {'username': 'Jaime'} #modelo me devuelve una row de un usuario
    #3.pasar datos del modelo a template i return
    profesores= [
        {'codi': 'PSD', 'name': 'David'},
        {'codi': 'MOL', 'name': 'Chemita'}
    ]

    asignatura = {
        'codi': 'IAW',
        'name': 'Implantacion de aplicaciones web',
        'profesor': 'David',
        'horari': 'dx-dj-dv'
    }
    return render_template('home.html', user=user, title='Hola', text='A', subject=asignatura, profesores=profesores)

#/game/<genre>
game = [
{'name': 'Sea of Stars',
     'genre': 'Indie'},
{'name': 'Alan Wake 2',
     'genre': 'Horror'},
{'name': 'Baldurs Gate 3',
     'genre': 'RPG'},
{'name': 'Dave the Diver',
     'genre': 'Indie'},
{'name': 'Resident Evil 4 Remake',
     'genre': 'Horror'},
{'name': 'Counter-Strike 2',
     'genre': 'FPS'}
]
'''
@app.route('/home')
def games_by_genre():
    return "<html><body><h1>Hola</h1></body></html>"



@app.route('/otrapagina')
def otrapagina():
    return "<html><body><h2>Hola Jaime!</h2></body></html>"\
           "<html><body><h1>Soy la otra pagina!</h1><a href='/'>Pagina Principal</a></body></html>"

@app.route('/')
def home_no_template():
    user = {'username' : 'Jaime'}
    return '''
        <html>
            <body>
                <h1>Hello, ''' + user['username'] + '''</h1>
                <ul>
                     <li><a href='/home'>Index</a></li>
                     <li><a href='/otrapagina'>Otrapagina</a></li>
                     <li><a href='/userprofile/Jaime'>Jaime</a></li>
                     <li><a href='/userprofile/Andrea'>Andrea</a></li>
                </ul>
            </body>
        </html>
    '''

'''
@app.route('/userprofile/<username>') #username es un parametro
#version inicial
def userprofile(username):
    return f'{username}'
'''

@app.route('/userprofile/<username>') #username es un parametro
#segunda version
def userprofile(username):
    users = {
        'Jaime': {
            'email': 'jaimedumas@gmail.com',
            'fecha_creacion': '01-02-2002'
        },
        'Andrea': {
            'email': 'andrea@gmail.com',
            'fecha_creacion': '01/02/2002'
        }
    }
    if username in users: #comprovamos si el modelo devuelve valor para el parametro username
        return f'{users[username]}' #redirigimos a template por pagina de usuario
    else:
        return 'usuario no existe' #redirigiremos a template de busqueda con mensaje de not found

if __name__ == '__main__':
    app.run()

