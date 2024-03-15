from flask import render_template, request

jogadores = []
jogos = []
gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

def init_app(app):
    # Definindo a rota principal
    @app.route('/')
    # Função que será executada ao acessar a rota
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                
            if request.form.get('jogo'):
                jogos.append(request.form.get('jogo'))
                
        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        return render_template('cadgames.html', gamelist=gamelist)