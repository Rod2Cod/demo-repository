from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class PostgreSQLRepository:
    def __init__(self, db):
        self.__db = db

    def saveElementoDomanda(self, elementoEntity: ElementoDomandaEntity) -> bool:
        try:
            self.__db.session.add(elementoEntity)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def loadElementoDomandaById(self, idElemento: int) -> ElementoDomandaEntity:
        return ElementoDomandaEntity.query.filter_by(id=idElemento).first()
    
    def deleteElementoDomanda(self, idElemento: int) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            self.__db.session.delete(elemento)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def loadAllElementiDomanda(self) -> set[ElementoDomandaEntity]:
        return set(ElementoDomandaEntity.query.all())
    
    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            elemento.domanda = domanda
            self.__db.session.commit()
            return True
        except:
            return False
    
    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            elemento.risposta = risposta
            self.__db.session.commit()
            return True
        except:
            return False    