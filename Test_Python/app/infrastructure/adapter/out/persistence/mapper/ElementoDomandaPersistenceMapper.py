from app.domain import ElementoDomanda, Domanda, Risposta, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class ElementoDomandaPersistenceMapper:

    def fromElementoDomandaEntity(self, entity: ElementoDomandaEntity) -> ElementoDomanda:
        return ElementoDomanda(idElemento=entity.id, 
                               domanda=Domanda(entity.domanda), 
                               risposta=Risposta(entity.risposta))

    def toElementoDomandaEntity(self, elemento: ElementoDomanda) -> ElementoDomandaEntity:
        return ElementoDomandaEntity(domanda=elemento.getDomanda().getText(), 
                                     risposta=elemento.getRisposta().getText())