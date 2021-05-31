import os

from flask import Flask


def create_app(test_config=None):
    # criar e configurar o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # carregue a configuração da instância, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carregue a configuração do teste se for aprovado
        app.config.from_mapping(test_config)

    # certifique-se de que a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # pagina simples com Olá mundo
    @app.route('/hello')
    def hello():
        return 'Olá, Mundo!'

    return app
    