from src.application.ExecuteTestUseCase import ExecuteTestOnSetUseCase
from src.application.ports.LLMPort import LLMPort
from src.application.ports.AlgoritmoValutazioneRisposte import AlgoritmoValutazioneRisposte
from src.application.ports.RisultatoTestPorts import SaveRisultatoTestPort
from src.application.ports.SetElementiDomandaPorts import GetSetElementiDomandaPort
from src.application.ports.ElementiDomandaPorts import GetElementoDomandaPort
from src.domain import RisultatoTest, RisultatoSingolaDomanda

# BOZZA DA MATCHARE CON IL TIPO DI RITORNO: Implementazione del caso d'uso per eseguire un test
class ExecuteTestOnSetService(ExecuteTestOnSetUseCase):
    def __init__(self,
                 llm: LLMPort,
                 valutatore: AlgoritmoValutazioneRisposte,
                 save_port: SaveRisultatoTestPort,
                 get_set_port: GetSetElementiDomandaPort,
                 get_elemento_port: GetElementoDomandaPort):
        self.llm = llm
        self.valutatore = valutatore
        self.save_port = save_port
        self.get_set_port = get_set_port
        self.get_elemento_port = get_elemento_port

    def executeTestOnSet(self, nomeSet: str) -> RisultatoTest:
        set_domande = self.get_set_port.getSetElementiDomandaByNome(nomeSet)
        risultati = []

        for id_domanda in set_domande.elementi:
            domanda = self.get_elemento_port.getElementoDomandaById(id_domanda)
            risposta_llm = self.llm.makeQuestion(domanda.domanda)
            valutazione = self.valutatore.evaluate(domanda.risposta, risposta_llm)
            risultato = RisultatoSingolaDomanda(domanda.id, risposta_llm, valutazione)
            risultati.append(risultato)

        risultato_test = RisultatoTest(risultati)
        self.save_port.saveRisultatoTest(risultato_test)
        return risultato_test
