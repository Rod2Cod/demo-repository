from typing import Set
from .UpdateElementiDomandaSetUseCase import UpdateElementiDomandaSetUseCase
from .UpdateElementiDomandaSetPort import UpdateElementiDomandaSetPort

class ServizioSetUpdateElementi(UpdateElementiDomandaSetUseCase):
    def __init__(self, porta_update_elementi: UpdateElementiDomandaSetPort):
        self.porta_update_elementi = porta_update_elementi

    def update_elementi_domanda(self, nome: str, elementi_id: Set[int]) -> bool:
        if not nome or not elementi_id:
            raise ValueError("Il nome e gli elementi non possono essere vuoti")
        
        return self.porta_update_elementi.update_elementi_domanda_associati(nome, elementi_id)
