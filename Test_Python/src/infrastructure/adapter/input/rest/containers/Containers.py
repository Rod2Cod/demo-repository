from src.infrastructure.adapter.input.rest.containers.ElementoDomandaContainer import ElementoDomandaContainer
from dependency_injector import containers, providers

class Containers(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(modules=["src.infrastructure.adapter.input.rest"])
    
    db = providers.Dependency()
    
    elementoDomandaContainer = providers.Container(ElementoDomandaContainer, db=db)