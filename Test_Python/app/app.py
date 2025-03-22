from flask import Flask
import os
from infrastructure.adapter.output.persistence.Extensions import db
from infrastructure.adapter.input.rest.ElementoDomandaControllers import elementoDomanda_blueprint
from infrastructure.adapter.input.rest.RisultatoTestControllers import risultatoTest_blueprint
from infrastructure.adapter.input.rest.ExecuteTestControllers import executeTest_blueprint

# Configuro Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "default_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Registro i blueprint (route inserite in altri file)
app.register_blueprint(elementoDomanda_blueprint)
app.register_blueprint(risultatoTest_blueprint)
app.register_blueprint(executeTest_blueprint)

# Inizializzo il database
db.init_app(app)

# Punto di ingresso
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea le tabelle se non esistono
    app.run(debug=True)  # Avvia il server Flask