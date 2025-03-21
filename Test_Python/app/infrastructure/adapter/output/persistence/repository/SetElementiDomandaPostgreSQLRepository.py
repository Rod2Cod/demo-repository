from app.infrastructure.adapter.output.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity

class SetElementiDomandaPostgreSQLRepository:
    def __init__(self, db):
        self.__db = db
        
    def saveSetElementiDomanda(self, setElementiEntity: SetElementiDomandaEntity) -> bool:
        try:
            self.__db.session.add(setElementiEntity)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def deleteSetElementiDomanda(self, nomeSet: str) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            self.__db.session.delete(setElementi)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def loadSetElementiDomandaByNome(self, nomeSet: str) -> SetElementiDomandaEntity:
        return SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
    
    def loadAllSetElementiDomanda(self) -> set[SetElementiDomandaEntity]:
        return set(SetElementiDomandaEntity.query.all())
    
    def updateNomeSetElementiDomanda(self, nomeSet: str, nuovoNomeSet: str) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            setElementi.nome = nuovoNomeSet
            self.__db.session.commit()
            return True
        except:
            return False
    
    def updateElementiSetElementiDomanda(self, nomeSet: str, elementi: set[ElementoDomandaEntity]) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            setElementi.elementi = elementi
            self.__db.session.commit()
            return True
        except:
            return False