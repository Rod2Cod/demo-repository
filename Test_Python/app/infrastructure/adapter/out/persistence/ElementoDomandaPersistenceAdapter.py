from app.application.ports.out import SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateDomandaElementoDomandaPort, UpdateRispostaElementoDomandaPort
from app.domain import ElementoDomanda
from app.infrastructure.adapter.out.persistence.mapper import ElementoDomandaPersistenceMapper

class ElementoDomandaPersistenceAdapter(
    SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateDomandaElementoDomandaPort, UpdateRispostaElementoDomandaPort
):
    def __init__(self, repository):
        self.__repository = repository
        self.__mapper = ElementoDomandaPersistenceMapper()

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