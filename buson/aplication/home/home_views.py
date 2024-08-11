from flask import Blueprint, render_template, session, flash, redirect, url_for
from horas import greetings
from user_on.comfig_user import is_user_logged_in


tela_home = Blueprint('home', __name__, template_folder='templates')
sair = Blueprint('logout', __name__)

@tela_home.route('/', methods=['GET'])
# @cache.cached(timeout=60)
def home():
    layout = None
    user_name = None
    
    msg = greetings()

    if is_user_logged_in():
        layout = session['user']
        user_name = session['user']['name']
      

        if len(user_name) > 10:
            user_name = user_name[:10]
            
    else:
        msg = greetings()

        
    return render_template('home.html', layout=layout, user_name=user_name, msg=msg)



        
@sair.route('/logout/')
def logout():
    session.pop('user', None)
    print("Usuário deslogado:", session.get('user'))  # Verifica se o usuário foi removido da sessão
    return redirect(url_for('home.home'))
