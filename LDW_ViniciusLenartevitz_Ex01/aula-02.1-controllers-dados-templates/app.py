# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Iniciando a função de rotas init_app passando o Flask como parâmetro
routes.init_app(app)

# Se for executado diretamente pelo interpretador (arquivo principal)
if __name__ == '__main__': 
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)
