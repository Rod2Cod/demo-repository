from dependency_injector import containers, providers
from src.application import AddElementoDomandaService, GetElementoDomandaService
from src.infrastructure.adapter.output.persistence.ElementoDomandaPersistenceAdapter import ElementoDomandaPersistenceAdapter
from src.infrastructure.adapter.output.persistence.repository.ElementoDomandaPostgreSQLRepository import ElementoDomandaPostgreSQLRepository

class ElementoDomandaContainer(containers.DeclarativeContainer):
    
    db = providers.Dependency()
    
    # Repository
    ElementoDomandaRepository = providers.Factory(ElementoDomandaPostgreSQLRepository, db=db)
    
    # Adapter
    ElementoDomandaAdapter = providers.Factory(ElementoDomandaPersistenceAdapter, repository=ElementoDomandaRepository)
    
    # Services
    AddElementoDomandaService = providers.Factory(AddElementoDomandaService, port=ElementoDomandaAdapter)
    GetElementoDomandaService = providers.Factory(GetElementoDomandaService, port=ElementoDomandaAdapter)