from flask import request, jsonify, Blueprint
from pydantic import ValidationError

from src.application.ports.input import AddRisultatoTestUseCase, GetRisultatoTestUseCase, GetAllRisultatiTestUseCase, GetAllRisultatiSingoleDomandeUseCase, GetRisultatoSingolaDomandaUseCase

risultatoTest_blueprint = Blueprint('risultatoTest_blueprint', __name__, url_prefix='/api')

class AddRisultatoTestController:
    def __init__(self, useCase: AddRisultatoTestUseCase):
        self.useCase = useCase

    @risultatoTest_blueprint.route('/risultatoTest/add', methods=['POST'])
    def addRisultatoTest(self):
        pass
        
class GetRisultatoTestController:
    def __init__(self, useCase: GetRisultatoTestUseCase):
        self.useCase = useCase

    @risultatoTest_blueprint.route('/risultatoTest/<int:id>', methods=['GET'])
    def getRisultatoTestById(self):
        try:
            id = request.args.get('id', type=int)
            risultato = self.useCase.getRisultatoTestById(id)
            return jsonify(risultato.serialize()), 200 if risultato else jsonify("Risultato non trovato."), 404
        except ValueError:
            return jsonify("L'id deve essere un intero.", 400)
    
class GetAllRisultatiTestController:
    def __init__(self, useCase: GetAllRisultatiTestUseCase):
        self.useCase = useCase

    @risultatoTest_blueprint.route('/risultatiTest', methods=['GET'])
    def getAllRisultatiTest(self):
        try:
            return self.useCase.getAllRisultatiTest()
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500
    
class GetAllRisultatiSingoleDomandeController:
    def __init__(self, useCase: GetAllRisultatiSingoleDomandeUseCase):
        self.useCase = useCase

    @risultatoTest_blueprint.route('/risultatiSingoleDomande/<int:id>', methods=['GET'])
    def getAllRisultatiSingoleDomandeByTestId(self):
        try:
            id = request.args.get('id', type=int)
            risultati = self.useCase.getAllRisultatiSingoleDomandeByTestId(id)
            return jsonify([risultato.serialize() for risultato in risultati]), 200 if risultati else jsonify("Set non trovato."), 404
        except ValueError:
            return jsonify("L'id deve essere un intero.", 400)
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500      
    
class GetRisultatoSingolaDomandaController:
    def __init__(self, useCase: GetRisultatoSingolaDomandaUseCase):
        self.useCase = useCase

    @risultatoTest_blueprint.route('/risultatoSingolaDomanda/<int:id>', methods=['GET'])
    def getRisultatoSingolaDomandaById(self):
        try:
            id = request.args.get('id', type=int)
            risultato = self.useCase.getRisultatoSingolaDomandaTestById(id)
            return jsonify(risultato.serialize()), 200 if risultato else jsonify("Risultato non trovato."), 404
        except ValueError:
            return jsonify("L'id deve essere un intero.", 400)
        except Exception:
            return jsonify("Si è verificato un errore nel server, riprova pià tardi"), 500