from dependency_injector import containers, providers
from src.application import AddElementoDomandaService, GetElementoDomandaService, GetAllElementiDomandaService, DeleteElementiDomandaService, UpdateElementoDomandaService
from src.infrastructure.adapter.output.persistence.ElementoDomandaPersistenceAdapter import ElementoDomandaPersistenceAdapter
from src.infrastructure.adapter.output.persistence.repository.ElementoDomandaPostgreSQLRepository import ElementoDomandaPostgreSQLRepository

class ElementoDomandaContainer(containers.DeclarativeContainer):
    
    """ Qui indico che mi deve arrivare una dipendenza db, che sarà fornita dall'esterno, in questo caso dal container principale """
    db = providers.Dependency()
    
    # Repository
    ElementoDomandaRepository = providers.Factory(ElementoDomandaPostgreSQLRepository, db=db)
    
    # Adapter
    ElementoDomandaAdapter = providers.Factory(ElementoDomandaPersistenceAdapter, repository=ElementoDomandaRepository)
    
    # Services
    AddElementoDomandaService = providers.Factory(AddElementoDomandaService, port=ElementoDomandaAdapter)
    GetElementoDomandaService = providers.Factory(GetElementoDomandaService, port=ElementoDomandaAdapter)
    GetAllElementiDomandaService = providers.Factory(GetAllElementiDomandaService, port=ElementoDomandaAdapter)
    DeleteElementiDomandaService = providers.Factory(DeleteElementiDomandaService, port=ElementoDomandaAdapter)
    UpdateElementoDomandaService = providers.Factory(UpdateElementoDomandaService, port=ElementoDomandaAdapter)