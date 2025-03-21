from app.infrastructure.adapter.output.persistence.domain import RisultatoTestEntity

class RisultatoTestPostgreSQLRepository:
    def __init__(self, db):
        self.__db = db
        
    def saveRisultatoTest(self, risultatoTestEntity: RisultatoTestEntity) -> bool:
        try:
            self.__db.session.add(risultatoTestEntity)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def loadRisultatoTestById(self, idRisultatoTest: int) -> RisultatoTestEntity:
        return RisultatoTestEntity.query.filter_by(id=idRisultatoTest).first()
    
    def deleteRisultatoTest(self, idRisultatoTest: int) -> bool:
        try:
            risultatoTest = RisultatoTestEntity.query.filter_by(id=idRisultatoTest).first()
            self.__db.session.delete(risultatoTest)
            self.__db.session.commit()
            return True
        except:
            return False
    
    def loadAllRisultatiTest(self) -> set[RisultatoTestEntity]:
        return set(RisultatoTestEntity.query.all())