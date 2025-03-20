from app.domain import ElementoDomanda, Domanda, Risposta, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class RisultatoSingolaDomandaPersistenceMapper:
    
    def fromRisultatoSingolaDomandaEntity(self, entity: RisultatoSingolaDomandaEntity) -> RisultatoSingolaDomanda:
        return RisultatoSingolaDomanda(id=entity.id, 
                                        domanda=entity.domanda, 
                                        risposta=entity.risposta, 
                                        rispostaLLM=entity.rispostaLLM, 
                                        score=entity.score, 
                                        metriche={"metrica1" : entity.metrica1,
                                                    "metrica2" : entity.metrica2,
                                                    "metrica3" : entity.metrica3,
                                                    "metrica4" : entity.metrica4,
                                                    "metrica5" : entity.metrica5,
                                                    "metrica6" : entity.metrica6})

    def toRisultatoSingolaDomandaEntity(self, risultato: RisultatoSingolaDomanda) -> RisultatoSingolaDomandaEntity:
        return RisultatoSingolaDomandaEntity(domanda=risultato.getDomanda(), 
                                                risposta=risultato.getRisposta(), 
                                                rispostaLLM=risultato.getRispostaLLM(), 
                                                score=risultato.getScore(), 
                                                metrica1=risultato.getMetriche()['metrica1'],
                                                metrica2=risultato.getMetriche()['metrica2'],
                                                metrica3=risultato.getMetriche()['metrica3'],
                                                metrica4=risultato.getMetriche()['metrica4'],
                                                metrica5=risultato.getMetriche()['metrica5'],
                                                metrica6=risultato.getMetriche()['metrica6'])