from .EditNomeSetElementiDomandaUseCase import EditNomeSetElementiDomandaUseCase
from .EditNomeSetElementiDomandaPort import EditNomeSetElementiDomandaPort

class ServizioSetEditNome(EditNomeSetElementiDomandaUseCase):
    def __init__(self, porta_edit_nome: EditNomeSetElementiDomandaPort):
        self.porta_edit_nome = porta_edit_nome

    def edit_nome(self, nome: str, nome_new: str) -> bool:
        if not nome or not nome_new:
            raise ValueError("Il nome originale e il nuovo nome non possono essere vuoti")
        
        if nome == nome_new:
            raise ValueError("Il nuovo nome deve essere diverso da quello originale")
        
        return self.porta_edit_nome.edit_nome_set(nome, nome_new)
