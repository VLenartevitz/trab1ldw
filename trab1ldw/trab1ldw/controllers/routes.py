from flask import render_template, request

jogadores = []
books = []
cursosList = [{'nome' : 'google cloud', 'horas' : 20, 'professor' : 'Deus'}]
livroslist = [{'Livros' : 'Harry'}]


def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/perfil', methods=['GET', 'POST'])
    def perfil():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('horas') and request.form.get('professor'):
                cursosList.append({'nome' : request.form.get('nome'), 'horas' : request.form.get('horas'), 'professor' : request.form.get('professor')})
        return render_template('perfil.html',cursosList=cursosList)
    

    @app.route('/livros', methods=['GET', 'POST'])
    def livros():
        livro = livroslist[0]
      
        if request.form.get('livro'):
            books.append(request.form.get('livro'))
                
        return render_template('livros.html',livro=livro, jogadores=jogadores, books=books
)
    

  