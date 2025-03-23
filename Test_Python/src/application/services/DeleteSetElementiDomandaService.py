from src.application.SetElementiDomandaUseCase import DeleteSetElementiDomandaUseCase
from src.application.ports.SetElementiDomandaPorts import DeleteSetElementiDomandaPort

class DeleteSetElementiDomandaService(DeleteSetElementiDomandaUseCase):
    def __init__(self, port: DeleteSetElementiDomandaPort):
        self.port = port

    def deleteSetElementiDomandaByNome(self, nome: str) -> bool:
        return self.port.deleteSetElementiDomandaByNome(nome)
