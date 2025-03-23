from abc import ABC, abstractmethod

class AlgoritmoValutazioneRisposte(ABC):

    @abstractmethod
    def evaluate(self, risposta_attesa: str, risposta_llm: str) -> dict[str, float]:
        pass
