from src.infrastructure.adapter.output.persistence.domain import ElementoDomandaEntity

class ElementoDomandaPostgreSQLRepository:
    def __init__(self, db):
        self.__db = db

    def saveElementoDomanda(self, elementoEntity: ElementoDomandaEntity) -> ElementoDomandaEntity:
        self.__db.session.add(elementoEntity)
        self.__db.session.commit()
        return elementoEntity
    
    def loadElementoDomandaById(self, idElemento: int) -> ElementoDomandaEntity:
        return ElementoDomandaEntity.query.filter_by(id=idElemento).first()
    
    def deleteElementiDomanda(self, idElementi: set[int]) -> None:
        ElementoDomandaEntity.query.filter(ElementoDomandaEntity.id.in_(idElementi)).delete(synchronize_session=False)
        self.__db.session.commit()
    
    def loadAllElementiDomanda(self) -> set[ElementoDomandaEntity]:
        return set(ElementoDomandaEntity.query.all())
    
    def updateElementoDomanda(self, idElemento: int, domanda: str, risposta: str) -> None:
        elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
        elemento.domanda = domanda
        elemento.risposta = risposta
        self.__db.session.commit()