from app.infrastructure.adapter.output.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class RisultatoSingolaDomandaPostgreSQLRepository:
    def __init__(self, db):
        self.__db = db
        
    def loadRisultatoSingolaDomandaTestById(self, idRisultatoSingolaDomanda: int) -> RisultatoSingolaDomandaEntity:
        return RisultatoSingolaDomandaEntity.query.filter_by(id=idRisultatoSingolaDomanda).first()
    
    def loadAllRisultatiSingolaDomandaByTestId(self, idRisultatoTest: int) -> set[RisultatoSingolaDomandaEntity]:
        return set(RisultatoSingolaDomandaEntity.query.filter_by(risultato_test_id=idRisultatoTest).all())