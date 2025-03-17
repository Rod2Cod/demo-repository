from app.application.ports.out import SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateDomandaElementoDomandaPort, UpdateRispostaElementoDomandaPort
from app.application.ports.out import SaveSetElementiDomandaPort, DeleteSetElementiDomandaPort, GetSetElementiDomandaPort, GetAllSetElementiDomandaPort, EditNomeSetElementiDomandaPort, UpdateElementiDomandaSetPort
from app.application.ports.out import SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity
from app.domain import ElementoDomanda, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.PersistenceMapper import PersistenceMapper

class PersistenceAdapter(
    SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateDomandaElementoDomandaPort, UpdateRispostaElementoDomandaPort,
    SaveSetElementiDomandaPort, DeleteSetElementiDomandaPort, GetSetElementiDomandaPort, GetAllSetElementiDomandaPort, EditNomeSetElementiDomandaPort, UpdateElementiDomandaSetPort,
    SaveRisultatoTestPort, GetRisultatoTestPort, GetAllRisultatiTestPort, GetAllRisultatiSingoleDomandeTestPort, GetRisultatoSingolaDomandaPort
):
    def __init__(self, repository):
        self.__repository = repository
        self.__mapper = PersistenceMapper()

    def saveElementoDomanda(self, elemento: ElementoDomanda) -> bool:
        self.__repository.saveElementoDomanda(self.__mapper.toElementoDomandaEntity(elemento))

    def getElementoDomandaById(self, idElemento: int) -> ElementoDomanda:
        return self.__mapper.fromElementoDomandaEntity(self.__repository.loadElementoDomandaById(idElemento))

    def deleteElementoDomanda(self, idElemento: int) -> bool:
        self.__repository.deleteElementoDomanda(idElemento)

    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        return {self.__mapper.fromElementoDomandaEntity(x) for x in self.__repository.loadAllElementiDomanda()}

    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        self.__repository.updateDomandaElementoDomanda(idElemento, domanda)

    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        self.__repository.updateRispostaElementoDomanda(idElemento, risposta)
        
    def saveSetElementiDomanda(self, setElementi: SetElementiDomanda) -> bool:
        self.__repository.saveSetElementiDomanda(self.__mapper.toSetElementiDomandaEntity(setElementi))

    def deleteSetElementiDomanda(self, nomeSet: str) -> bool:
        self.__repository.deleteSetElementiDomanda(nomeSet)

    def getSetElementiDomandaByNome(self, nomeSet: str) -> SetElementiDomanda:
        return self.__mapper.fromSetElementiDomandaEntity(self.__repository.loadSetElementiDomandaByNome(nomeSet))

    def getAllSetElementiDomanda(self) -> set[SetElementiDomanda]:
        return self.__repository.loadAllSetElementiDomanda()

    def editNomeSetElementiDomanda(self, nomeSet: str, nuovoNomeSet: str) -> bool:
        self.__repository.updateNomeSetElementiDomanda(nomeSet, nuovoNomeSet)

    def updateElementiSetElementiDomanda(self, nomeSet: str, elementi: set[ElementoDomanda]) -> bool:
        self.__repository.updateElementiSetElementiDomanda(nomeSet, elementi)

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