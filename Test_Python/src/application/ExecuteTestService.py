from src.application.ExecuteTestUseCase import ExecuteTestUseCase
from src.application.ports.LLMPort import LLMPort
from src.application.ports.AlgoritmoValutazioneRisposte import AlgoritmoValutazioneRisposte
from src.application.ports.RisultatoTestPorts import SaveRisultatoTestPort
from src.application.ports.SetElementiDomandaPorts import GetAllSetElementiDomandaPort
from src.domain import RisultatoTest, RisultatoSingolaDomanda


# BOZZA DA MATCHARE CON IL TIPO DI RITORNO: Implementazione del caso d'uso per eseguire un test
class ExecuteTestService(ExecuteTestUseCase):
    def __init__(self,
                 llm: LLMPort,
                 valutatore: AlgoritmoValutazioneRisposte,
                 save_port: SaveRisultatoTestPort,
                 get_set_port: GetAllSetElementiDomandaPort):
        self.llm = llm
        self.valutatore = valutatore
        self.save_port = save_port
        self.get_set_port = get_set_port

    def executeTest(self) -> RisultatoTest:
        # logica per recuperare tutte le domande
        all_sets = self.get_set_port.getAllSetElementiDomanda()
        domande = next(iter(all_sets)).elementi  # esempio: prende il primo set

        risultati = []
        for domanda in domande:
            risposta_llm = self.llm.makeQuestion(domanda.domanda)
            valutazione = self.valutatore.evaluate(domanda.risposta, risposta_llm)
            risultato = RisultatoSingolaDomanda(domanda.id, risposta_llm, valutazione)
            risultati.append(risultato)

        risultato_test = RisultatoTest(risultati)
        self.save_port.saveRisultatoTest(risultato_test)
        return risultato_test
