from typing import Set
from .GetAllSetElementiDomandaUseCase import GetAllSetElementiDomandaUseCase
from .GetAllSetElementiDomandaPort import GetAllSetElementiDomandaPort
from .SetElementiDomanda import SetElementiDomanda

class ServizioSetGetAllElementi(GetAllSetElementiDomandaUseCase):
    def __init__(self, porta_get_all_set: GetAllSetElementiDomandaPort):
        self.porta_get_all_set = porta_get_all_set

    def get_all_set(self) -> Set[SetElementiDomanda]:
        return self.porta_get_all_set.get_all_set_elementi_domanda()
