from app.application.ports.output import SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateElementoDomandaPort
from app.domain import ElementoDomanda
from app.infrastructure.adapter.output.persistence.mapper import ElementoDomandaPersistenceMapper

class ElementoDomandaPersistenceAdapter(
    SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementoDomandaPort, GetAllElementiDomandaPort, UpdateElementoDomandaPort
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

    def updateElementoDomanda(self, idElemento: int, domanda: str, risposta: str) -> bool:
        self.__repository.updateElementoDomanda(idElemento, domanda, risposta)