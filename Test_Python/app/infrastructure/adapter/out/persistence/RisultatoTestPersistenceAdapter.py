from app.application.ports.out import SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
from app.domain import RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.mapper import RisultatoSingolaDomandaPersistenceMapper, RisultatoTestPersistenceMapper

class RisultatoTestPersistenceAdapter(
    SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
):
    def __init__(self, repositoryTest, repositorySingolaDomanda):
        self.__repositoryTest = repositoryTest
        self.__repositorySingolaDomanda = repositorySingolaDomanda
        self.__mapperTest = RisultatoTestPersistenceMapper()
        self.__mapperSingolaDomanda = RisultatoSingolaDomandaPersistenceMapper()
        
    def saveRisultatoTest(self, risultatoTest: RisultatoTest) -> bool:
        self.__repositoryTest.saveRisultatoTest(self.__mapperTest.toRisultatoTestEntity(risultatoTest))

    def getRisultatoTestById(self, idRisultatoTest: int) -> RisultatoTest:
        return self.__mapperTest.fromRisultatoTestEntity(self.__repositoryTest.loadRisultatoTestById(idRisultatoTest))

    def deleteRisultatoTest(self, idRisultatoTest: int) -> bool:
        self.__repositoryTest.deleteRisultatoTest(idRisultatoTest)

    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        return (self.__mapperTest.fromRisultatoTestEntity(risultatoTest) for risultatoTest in self.__repositoryTest.loadAllRisultatiTest())
    
    def getAllRisultatiSingoleDomandeByTestId(self, idTest: int) -> set[RisultatoSingolaDomanda]:
        return (self.__mapperSingolaDomanda.fromRisultatoSingolaDomandaEntity(risultatoSingolaDomanda) for risultatoSingolaDomanda in self.__repositorySingolaDomanda.loadAllRisultatiSingolaDomandaByTestId(idTest))

    def getRisultatoSingolaDomandaTestById(self, idRisultatoSingolaDomanda: int) -> RisultatoSingolaDomanda:
        return self.__mapperSingolaDomanda.fromRisultatoSingolaDomandaEntity(self.__repositorySingolaDomanda.loadRisultatoSingolaDomandaTestById(idRisultatoSingolaDomanda))