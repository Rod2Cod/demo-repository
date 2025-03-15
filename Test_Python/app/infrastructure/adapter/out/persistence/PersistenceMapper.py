from app.domain import ElementoDomanda, Domanda, Risposta, SetElementiDomanda, RisultatoTest, RisultatoSingolaDomanda
from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class PersistenceMapper:
    def __init__(self):
        pass

    def fromElementoDomandaEntity(self, entity: ElementoDomandaEntity) -> ElementoDomanda:
        return ElementoDomanda(idElemento=entity.id, 
                               domanda=Domanda(entity.domanda), 
                               risposta=Risposta(entity.risposta))

    def toElementoDomandaEntity(self, elemento: ElementoDomanda) -> ElementoDomandaEntity:
        return ElementoDomandaEntity(domanda=elemento.getDomanda().getText(), 
                                     risposta=elemento.getRisposta().getText())

    def fromSetElementiDomandaEntity(self, entity: SetElementiDomandaEntity) -> SetElementiDomanda:
        return SetElementiDomanda(nome=entity.nome, 
                                  elementi=set([self.fromElementoDomandaEntity(elemento) for elemento in entity.elementi]))

    def toSetElementiDomandaEntity(self, setElementi: SetElementiDomanda) -> SetElementiDomandaEntity:
        return SetElementiDomandaEntity(nome=setElementi.getNome(), 
                                        elementi=set([self.toElementoDomandaEntity(elemento) for elemento in setElementi.getElementi()]))

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