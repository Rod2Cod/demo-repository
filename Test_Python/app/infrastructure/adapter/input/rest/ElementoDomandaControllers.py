from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from pydantic import ValidationError

from app.application.ports.input import AddElementoDomandaUseCase, GetElementoDomandaUseCase, GetAllElementiDomandaUseCase, DeleteElementiDomandaUseCase, UpdateElementoDomandaUseCase

elementoDomanda_blueprint = Blueprint('elementoDomanda_blueprint', __name__, url_prefix='/api')

class AddElementoDomandaController:
    def __init__(self, useCase: AddElementoDomandaUseCase):
        self.useCase = useCase

    @elementoDomanda_blueprint.route('/domande', methods=['POST'])
    def addElementoDomanda(self):
        try:
            # prendo domanda e risposta dal body della richiesta, se non presenti ritorna BadRequest
            domanda = request.json['domanda']
            risposta = request.json['risposta']
            elemento = self.useCase.addElementoDomanda(domanda, risposta)
            # se errore da adapter in poi
            return jsonify("Elemento aggiunto con successo"), 201 if elemento else jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500
        # se errore di validazione nella business logic
        except ValidationError as e:
            return jsonify(e.errors(), 400)
        except BadRequest:
            return jsonify("Domanda e risposta sono campi obbligatori.", 400)
    
class GetElementoDomandaController:
    def __init__(self, useCase: GetElementoDomandaUseCase):
        self.useCase = useCase

    @elementoDomanda_blueprint.route('/domande/<int:id>', methods=['GET'])
    def getElementoDomandaById(self, id: int):
        try:
            id = request.args.get('id', type=int)
            elemento = self.useCase.getElementoDomandaById(id)
            return jsonify(elemento.serialize()), 200 if elemento else jsonify("Elemento non trovato."), 404
        except ValueError:
            return jsonify("L'id deve essere un intero.", 400)
    
class GetAllElementiDomandaController:
    def __init__(self, useCase: GetAllElementiDomandaUseCase):
        self.useCase = useCase

    @elementoDomanda_blueprint.route('/domande', methods=['GET'])
    def getAllElementiDomanda(self):
        try:
            elementi = self.useCase.getAllElementiDomanda()
            return jsonify([elemento.serialize() for elemento in elementi]), 200
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500
    
class DeleteElementiDomandaController:
    def __init__(self, useCase: DeleteElementiDomandaUseCase):
        self.useCase = useCase

    @elementoDomanda_blueprint.route('/domande/delete', methods=['POST'])
    def deleteElementoDomanda(self):
        try:
            ids = request.json['ids']
            return self.useCase.deleteElementiDomandaById(ids) if not ids else jsonify("Ids è un campo obbligatorio.", 400)
        except BadRequest:
            return jsonify("Ids è un campo obbligatorio.", 400)
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500
        except ValueError:
            return jsonify("Gli id devono essere interi.", 400)
    
class UpdateElementoDomandaController:
    def __init__(self, useCase: UpdateElementoDomandaUseCase):
        self.useCase = useCase

    @elementoDomanda_blueprint.route('/domanda/<int:id>', methods=['PUT'])
    def updateElementoDomanda(self):
        try:
            id = request.args.get('id', type=int)
            domanda = request.json['domanda']
            risposta = request.json['risposta']
            return self.useCase.updateElementoDomanda(id, domanda, risposta) if not id else jsonify("Id è un campo obbligatorio.", 400)
        except BadRequest:
            return jsonify("Domanda e risposta sono campi obbligatori.", 400)
        except ValidationError as e:
            return jsonify(e.errors(), 400)
        except ValueError:
            return jsonify("L'id deve essere un intero.", 400)
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500