from app.application.ports.output import SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
from app.domain import RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.output.persistence.mapper import RisultatoSingolaDomandaPersistenceMapper, RisultatoTestPersistenceMapper
from sqlalchemy.exc import SQLAlchemyError

class RisultatoTestPersistenceAdapter(
    SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
):
    def __init__(self, repositoryTest, repositorySingolaDomanda):
        self.__repositoryTest = repositoryTest
        self.__repositorySingolaDomanda = repositorySingolaDomanda
        self.__mapperSingolaDomanda = RisultatoSingolaDomandaPersistenceMapper()
        self.__mapperTest = RisultatoTestPersistenceMapper(self.__mapperSingolaDomanda)
        
    def saveRisultatoTest(self, risultatoTest: RisultatoTest) -> bool:
        try:
            self.__repositoryTest.saveRisultatoTest(self.__mapperTest.toRisultatoTestEntity(risultatoTest))
            return True
        except Exception:
            return False
        except SQLAlchemyError:
            return False

    def getRisultatoTestById(self, idRisultatoTest: int) -> RisultatoTest:
        try:
            return self.__mapperTest.fromRisultatoTestEntity(self.__repositoryTest.loadRisultatoTestById(idRisultatoTest))
        except Exception:
            return None
        except SQLAlchemyError:
            return None


    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        try:
            return set(self.__mapperTest.fromRisultatoTestEntity(risultatoTest) for risultatoTest in self.__repositoryTest.loadAllRisultatiTest())
        except Exception:
            return None
        except SQLAlchemyError:
            return None
    
    def getAllRisultatiSingoleDomandeByTestId(self, idTest: int) -> set[RisultatoSingolaDomanda]:
        try:
            return set(self.__mapperSingolaDomanda.fromRisultatoSingolaDomandaEntity(risultatoSingolaDomanda) for risultatoSingolaDomanda in self.__repositorySingolaDomanda.loadAllRisultatiSingolaDomandaByTestId(idTest))
        except Exception:
            return None
        except SQLAlchemyError:
            return None

    def getRisultatoSingolaDomandaTestById(self, idRisultatoSingolaDomanda: int) -> RisultatoSingolaDomanda:
        try:
            return self.__mapperSingolaDomanda.fromRisultatoSingolaDomandaEntity(self.__repositorySingolaDomanda.loadRisultatoSingolaDomandaTestById(idRisultatoSingolaDomanda))
        except Exception:
            return None
        except SQLAlchemyError:
            return None