from .GetSetElementiDomandaUseCase import GetSetElementiDomandaUseCase
from .GetSetElementiDomandaPort import GetSetElementiDomandaPort
from .SetElementiDomanda import SetElementiDomanda

class ServizioSetGetElementi(GetSetElementiDomandaUseCase):
    def __init__(self, porta_get_set: GetSetElementiDomandaPort):
        self.porta_get_set = porta_get_set

    def get_set_by_nome(self, nome: str) -> SetElementiDomanda:
        if not nome:
            raise ValueError("Il nome del set non può essere vuoto")
        
        set_elementi = self.porta_get_set.get_set_elementi_domanda_by_nome(nome)
        if not set_elementi:
            raise KeyError(f"Set con nome '{nome}' non trovato")
        
        return set_elementi
