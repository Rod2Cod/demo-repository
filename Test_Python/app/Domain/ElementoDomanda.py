from Risposta import Risposta
from Domanda import Domanda

class ElementoDomanda:
    def __init__(self, domanda: str, risposta: str, id: int):
        self.__domanda = Domanda(domanda)
        self.__risposta = Risposta(risposta)
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def getDomanda(self) -> Domanda:
        return self.__domanda
    
    def getRisposta(self) -> Risposta:
        return self.__risposta

    def setDomanda(self, domanda: str):
        self.__domanda.setText(domanda)

    def setRisposta(self, risposta: str):
        self.__risposta.setText(risposta)