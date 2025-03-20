from typing import Set
from .AddSetElementiDomandaUseCase import AddSetElementiDomandaUseCase
from .SaveSetElementiDomandaPort import SaveSetElementiDomandaPort
from .SetElementiDomanda import SetElementiDomanda

class ServizioSetAddElementi(AddSetElementiDomandaUseCase):
    def __init__(self, porta_save_set: SaveSetElementiDomandaPort):
        self.porta_save_set = porta_save_set

    def add_set(self, nome: str, elementi_id: Set[int]) -> bool:
        if not nome or not elementi_id:
            raise ValueError("Nome e elementi non possono essere vuoti")
        
        set_elementi = SetElementiDomanda(nome=nome, elementi_id=elementi_id)
        return self.porta_save_set.save_set_elementi_domanda(set_elementi)