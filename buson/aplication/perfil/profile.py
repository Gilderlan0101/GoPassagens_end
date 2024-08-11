from flask import Blueprint, flash, render_template, redirect, url_for, session
from user_on.comfig_user import is_user_logged_in
from cache_routes.cache import cache

profile = Blueprint('account', __name__, template_folder='templates')

@profile.route('/account/')
@cache.cached(timeout=60)
def account():

    if not is_user_logged_in():
        flash("Você precisa estar logado para acessar essa página.", "warning")
        return redirect(url_for('login.login'))
    
  
    usuario = Usuario(session['user']['name'])
   
    return usuario.date_user()

class Usuario:
    def __init__(self, name):
        self.name = name
        self.user_name = None
        self.email = None
        self.tel = None
        
    def date_user(self):
        
        self.user_name = session['user']['name']
        self.email = session['user']['email']
        self.tel = session['user']['phone']

        
        return render_template(
            'account.html', user_name=self.user_name, user_email=self.email,
            user_tel=self.tel
         )
