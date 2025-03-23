from src.application.ElementoDomandaUseCase import UpdateElementoDomandaUseCase
from src.application.ports.ElementiDomandaPorts import UpdateElementoDomandaPort

class UpdateElementoDomandaService(UpdateElementoDomandaUseCase):
    def __init__(self, update_port: UpdateElementoDomandaPort):
        self.update_port = update_port

    def updateElementoDomandaById(self, id: int, domanda: str, risposta: str) -> bool:
        return self.update_port.updateElementoDomandaById(id, domanda, risposta)
