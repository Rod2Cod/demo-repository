from app.domain import ElementoDomanda, Domanda, Risposta, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class SetElementiDomandaPersistenceMapper:
    
    def fromSetElementiDomandaEntity(self, entity: SetElementiDomandaEntity) -> SetElementiDomanda:
        return SetElementiDomanda(nome=entity.nome, 
                                  elementi=set([self.fromElementoDomandaEntity(elemento) for elemento in entity.elementi]))

    def toSetElementiDomandaEntity(self, setElementi: SetElementiDomanda) -> SetElementiDomandaEntity:
        return SetElementiDomandaEntity(nome=setElementi.getNome(), 
                                        elementi=set([self.toElementoDomandaEntity(elemento) for elemento in setElementi.getElementi()]))