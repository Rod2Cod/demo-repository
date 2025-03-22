from app.application.ports.output import SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementiDomandaPort, GetAllElementiDomandaPort, UpdateElementoDomandaPort
from app.domain import ElementoDomanda
from app.infrastructure.adapter.output.persistence.mapper import ElementoDomandaPersistenceMapper
from sqlalchemy.exc import SQLAlchemyError

class ElementoDomandaPersistenceAdapter(
    SaveElementoDomandaPort, GetElementoDomandaPort, DeleteElementiDomandaPort, GetAllElementiDomandaPort, UpdateElementoDomandaPort
):
    def __init__(self, repository):
        self.__repository = repository
        self.__mapper = ElementoDomandaPersistenceMapper()

    def saveElementoDomanda(self, elemento: ElementoDomanda) -> ElementoDomanda:
        try:
            return self.__mapper.fromElementoDomandaEntity(self.__repository.saveElementoDomanda(self.__mapper.toElementoDomandaEntity(elemento)))
        # problema nel database
        except SQLAlchemyError:
            return None
        except Exception:
            return None

    def getElementoDomandaById(self, idElemento: int) -> ElementoDomanda:
        try:
            return self.__mapper.fromElementoDomandaEntity(self.__repository.loadElementoDomandaById(idElemento))
        # problema nel database
        except SQLAlchemyError:
            return None
        except Exception:
            return None

    def deleteElementiDomanda(self, idElementi: set[int]) -> bool:
        try:
            self.__repository.deleteElementoDomanda(idElementi)
            return True
        # problema nel database
        except SQLAlchemyError:
            return False
        except Exception:
            return False

    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        try:
            return set(self.__mapper.fromElementoDomandaEntity(x) for x in self.__repository.loadAllElementiDomanda())
        # problema nel database
        except SQLAlchemyError:
            return None
        except Exception:
            return None

    def updateElementoDomanda(self, idElemento: int, domanda: str, risposta: str) -> bool:
        try:
            self.__repository.updateElementoDomanda(idElemento, domanda, risposta)
            return True
        # problema nel database
        except SQLAlchemyError:
            return False