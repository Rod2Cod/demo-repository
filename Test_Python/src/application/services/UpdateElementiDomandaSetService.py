from src.application.SetElementiDomandaUseCase import UpdateElementiDomandaSetUseCase
from src.application.ports.SetElementiDomandaPorts import UpdateElementiDomandaSetPort

class UpdateElementiDomandaSetService(UpdateElementiDomandaSetUseCase):
    def __init__(self, port: UpdateElementiDomandaSetPort):
        self.port = port

    def updateElementiDomandaSet(self, nome: str, elementi: set[int]) -> bool:
        return self.port.updateElementiDomandaSet(nome, elementi)
