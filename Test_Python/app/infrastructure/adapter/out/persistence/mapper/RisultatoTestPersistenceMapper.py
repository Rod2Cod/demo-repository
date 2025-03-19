from app.domain import RisultatoTest
from app.infrastructure.adapter.out.persistence.domain import RisultatoTestEntity
from app.infrastructure.adapter.out.persistence.mapper import RisultatoSingolaDomandaPersistenceMapper

class RisultatoTestPersistenceMapper:
    def __init__(self):
        self.__mapperRisultatoSingolaDomanda = RisultatoSingolaDomandaPersistenceMapper()
    
    def fromRisultatoTestEntity(self, entity: RisultatoTestEntity) -> RisultatoTest:
        return RisultatoTest(id=entity.id, 
                            score=entity.score, 
                            LLM=entity.LLM, 
                            dataEsecuzione=entity.data, 
                            nomeSet=entity.nomeSet, 
                            risultatiDomande=set([self.__mapperRisultatoSingolaDomanda.fromRisultatoSingolaDomandaEntity(risultato) for risultato in entity.risultati]))

    def toRisultatoTestEntity(self, risultato: RisultatoTest) -> RisultatoTestEntity:
        return RisultatoTestEntity(score=risultato.getScore(), 
                                  LLM=risultato.getLLM(), 
                                  data=risultato.getDataEsecuzione(), 
                                  nomeSet=risultato.getNomeSet(), 
                                  risultati=set([self.__mapperRisultatoSingolaDomanda.toRisultatoSingolaDomandaEntity(risultato) for risultato in risultato.getRisultatiDomande()]) )