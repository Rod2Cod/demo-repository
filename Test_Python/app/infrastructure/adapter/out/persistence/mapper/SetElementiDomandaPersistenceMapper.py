from app.domain import SetElementiDomanda
from app.infrastructure.adapter.out.persistence.domain import SetElementiDomandaEntity
from app.infrastructure.adapter.out.persistence.mapper import ElementoDomandaPersistenceMapper

class SetElementiDomandaPersistenceMapper:
    def __init__(self):
        self.__mapperElementoDomanda = ElementoDomandaPersistenceMapper()
    
    def fromSetElementiDomandaEntity(self, entity: SetElementiDomandaEntity) -> SetElementiDomanda:
        return SetElementiDomanda(nome=entity.nome, 
                                  elementi=set([self.__mapperElementoDomanda.fromElementoDomandaEntity(elemento) for elemento in entity.elementi]))

    def toSetElementiDomandaEntity(self, setElementi: SetElementiDomanda) -> SetElementiDomandaEntity:
        return SetElementiDomandaEntity(nome=setElementi.getNome(), 
                                        elementi=set([self.__mapperElementoDomanda.toElementoDomandaEntity(elemento) for elemento in setElementi.getElementi()]))