from app.application.ports.out import SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity
from app.domain import ElementoDomanda, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.mapper import RisultatoSingolaDomandaPersistenceMapper, RisultatoTestPersistenceMapper

class RisultatoTestPersistenceAdapter(
    SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
):
    def __init__(self, repository):
        self.__repository = repository
        self.__mapperTest = RisultatoTestPersistenceMapper()
        self.__mapperSingolaDomanda = RisultatoSingolaDomandaPersistenceMapper()
        
    def saveRisultatoTest(self, risultatoTest: RisultatoTest) -> bool:
        self.__repository.saveRisultatoTest(self.__mapper.toRisultatoTestEntity(risultatoTest))

    def getRisultatoTestById(self, idRisultatoTest: int) -> RisultatoTest:
        return self.__repository.loadRisultatoTestById(idRisultatoTest)

    def deleteRisultatoTest(self, idRisultatoTest: int) -> bool:
        self.__repository.deleteRisultatoTest(idRisultatoTest)

    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        return self.__repository.loadAllRisultatiTest()
    
    def getAllRisultatiSingolaDomandaByTestId(self, idTest: int) -> set[RisultatoSingolaDomanda]:
        return self.__repository.loadAllRisultatiSingolaDomandaByTestId(idTest)

    def getRisultatoSingolaDomandaTestById(self, idRisultatoSingolaDomanda: int) -> RisultatoSingolaDomanda:
        return self.__repository.loadRisultatoSingolaDomandaTestById(idRisultatoSingolaDomanda)