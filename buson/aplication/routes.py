from flask import Flask
from login_views.login_user import tela_login
from home.home_views import tela_home,  sair
from orders.order_views import tela_pedidos
from registre.registre_views import tela_cadastro
from registre.verify_user.verify_account import tela_verifca
from config.comfig_tools import key_projecto
from perfil.profile import profile
from cache_routes.cache import cache, config


app = Flask(__name__)
app.secret_key = key_projecto()


app.register_blueprint(tela_home)
app.register_blueprint(tela_login)
app.register_blueprint(tela_pedidos)
app.register_blueprint(tela_cadastro)
app.register_blueprint(tela_verifca)
app.register_blueprint(sair)
app.register_blueprint(profile)

# Configurações de cache
app.config.from_mapping(config)
cache.init_app(app) 




@app.after_request
def add_cache_headers(response):
    if response.content_type.startswith('image'):
        response.headers['Cache-Control'] = 'public, max-age=31536000'  # 1 year
    return response
if __name__ == '__main__':
    app.run(debug=True, port=5000)