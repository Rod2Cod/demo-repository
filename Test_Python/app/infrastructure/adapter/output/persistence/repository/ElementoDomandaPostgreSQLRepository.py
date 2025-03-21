from app.infrastructure.adapter.output.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class ElementoDomandaPostgreSQLRepository:
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
    
    def updateElementoDomanda(self, idElemento: int, domanda: str, risposta: str) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            elemento.domanda = domanda
            elemento.ristposta = risposta
            self.__db.session.commit()
            return True
        except:
            return False