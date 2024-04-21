from flask import Flask, make_response, redirect, render_template, request, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная',
     'url': 'index'},
    {'name': 'Обо мне',
     'url': 'about'},
     {'name': 'Каталог',
     'url': 'catalog'},
     {'name': 'Контакты',
     'url': 'contacts'},
     {'name': 'Авторизация',
      'url': "login"} 
]

@app.route('/')
def index():
    context = {
        'title': "Главная",
        'menu': menu
    }
    return render_template('index.html', **context)

@app.route('/about/')
def about():
    context = {
        'title': "Обо мне",
        'menu': menu
    }
    return render_template('about.html', **context)

@app.route('/catalog/')
def catalog():
    context = {
        'title': "Каталог",
        'menu': menu
    }
    return render_template('catalog.html',**context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': "Контакты",
        'menu': menu
    }
    return render_template('contacts.html',**context )

@app.route('/login/')
def login(): 
    context = {
        'title': "Вход",
        'menu': menu
    }
    return render_template('login.html', **context)


@app.post('/login/') # type: ignore
def login_post():
    name = request.form.get('name')
    phone = request.form.get('phone')
    context = {
        'title': "Вход",
        'menu': menu,
        'name': name
    }
    response = make_response(render_template('hello.html', **context))
    response.set_cookie('username', name)
    response.set_cookie('phone', phone) 
    return response


@app.route('/exit/')
def exit():
    responce = make_response(redirect(url_for('index')))
    responce.delete_cookie('username')
    responce.delete_cookie('phone')


    return responce


if __name__ == "__main__":
    app.run(debug=True)
