from flask import Flask
from src.infrastructure.adapter.input.rest.containers.Containers import Containers
from src.infrastructure.adapter.output.persistence.Extensions import db
from src.infrastructure.adapter.input.rest.ElementoDomandaControllers import elementoDomanda_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "default_secret_key"
    
    # Configuro database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost:5432/progetto'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Configuro dependency injection
    container = Containers()
    
    container.db.override(db)
    
    app.container = container
    
    with app.app_context():
        from src.infrastructure.adapter.output.persistence.domain import ElementoDomandaEntity
        db.create_all()
    
    # Registro i blueprint (route inserite in altri file)
    app.register_blueprint(elementoDomanda_blueprint)
    
    print(app.url_map)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)