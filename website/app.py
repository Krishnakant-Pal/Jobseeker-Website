from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'something'

    
    from .routes import home
    from .routes import login
    from .signup import signup
    

    
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    
    return app

    