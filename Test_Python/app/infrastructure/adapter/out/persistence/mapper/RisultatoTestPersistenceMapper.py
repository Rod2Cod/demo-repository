from app.domain import ElementoDomanda, Domanda, Risposta, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class RisultatoTestPersistenceMapper:
    
    def fromRisultatoTestEntity(self, entity: RisultatoTestEntity) -> RisultatoTest:
        return RisultatoTest(id=entity.id, 
                            score=entity.score, 
                            LLM=entity.LLM, 
                            dataEsecuzione=entity.data, 
                            nomeSet=entity.nomeSet, 
                            risultatiDomande=set([self.fromRisultatoSingolaDomandaEntity(risultato) for risultato in entity.risultati]))

    def toRisultatoTestEntity(self, risultato: RisultatoTest) -> RisultatoTestEntity:
        return RisultatoTestEntity(score=risultato.getScore(), 
                                  LLM=risultato.getLLM(), 
                                  data=risultato.getDataEsecuzione(), 
                                  nomeSet=risultato.getNomeSet(), 
                                  risultati=set([self.toRisultatoSingolaDomandaEntity(risultato) for risultato in risultato.getRisultatiDomande()]) )