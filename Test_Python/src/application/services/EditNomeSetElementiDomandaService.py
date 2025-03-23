from src.application.SetElementiDomandaUseCase import EditNomeSetElementiDomandaUseCase
from src.application.ports.SetElementiDomandaPorts import EditNomeSetElementiDomandaPort

class EditNomeSetElementiDomandaService(EditNomeSetElementiDomandaUseCase):
    def __init__(self, port: EditNomeSetElementiDomandaPort):
        self.port = port

    def editNomeSetElementiDomanda(self, nome: str, newNome: str) -> bool:
        return self.port.editNomeSetElementiDomanda(nome, newNome)
