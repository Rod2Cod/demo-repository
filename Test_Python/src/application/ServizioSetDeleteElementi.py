from .DeleteSetElementiDomandaUseCase import DeleteSetElementiDomandaUseCase
from .DeleteSetElementiDomandaPort import DeleteSetElementiDomandaPort

class ServizioSetDeleteElementi(DeleteSetElementiDomandaUseCase):
    def __init__(self, porta_delete_set: DeleteSetElementiDomandaPort):
        self.porta_delete_set = porta_delete_set

    def delete_set_by_nome(self, nome: str) -> bool:
        if not nome:
            raise ValueError("Il nome del set non può essere vuoto")
        
        return self.porta_delete_set.delete_set_elementi_domanda_by_nome(nome)
