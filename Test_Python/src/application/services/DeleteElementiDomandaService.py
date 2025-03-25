from src.application.ElementoDomandaUseCase import DeleteElementiDomandaUseCase
from src.application.ports.ElementiDomandaPorts import DeleteElementiDomandaPort

class DeleteElementiDomandaService(DeleteElementiDomandaUseCase):
    def __init__(self, delete_port: DeleteElementiDomandaPort):
        self.delete_port = delete_port

    def deleteElementiDomandaById(self, Ids: set[int]) -> bool:
        return self.delete_port.deleteElementiDomandaById(Ids)
