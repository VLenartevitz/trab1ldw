from flask import render_template, request

jogadores = []
jogos = []
cursosList = [{'nome' : 'google cloud', 'horas' : 20, 'professor' : 'Deus'}]

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
    

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                
            if request.form.get('jogo'):
                jogos.append(request.form.get('jogo'))
                
        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
    
    

  