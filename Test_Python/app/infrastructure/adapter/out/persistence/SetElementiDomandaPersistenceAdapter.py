from app.application.ports.out import SaveSetElementiDomandaPort, DeleteSetElementiDomandaPort, GetSetElementiDomandaPort, GetAllSetElementiDomandaPort, EditNomeSetElementiDomandaPort, UpdateElementiDomandaSetPort
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity
from app.domain import ElementoDomanda, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.mapper import SetElementiDomandaPersistenceMapper

class SetElementiDomandaPersistenceAdapter(
    SaveSetElementiDomandaPort, DeleteSetElementiDomandaPort, GetSetElementiDomandaPort, GetAllSetElementiDomandaPort, EditNomeSetElementiDomandaPort, UpdateElementiDomandaSetPort
):
    def __init__(self, repository):
        self.__repository = repository
        self.__mapper = SetElementiDomandaPersistenceMapper()
        
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