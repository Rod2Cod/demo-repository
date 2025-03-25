from src.infrastructure.adapter.input.rest.containers.ElementoDomandaContainer import ElementoDomandaContainer
from dependency_injector import containers, providers

class Containers(containers.DeclarativeContainer):
    
    """
    Definisco il wiring (a quali moduli dovrò fornire le dipendenze).
    Se scrivo questo quando istanzio il container (container = Containers()), 
    esso chiamerà automaticamente in application container.wire con la configurazione che ho definito qua
    """
    wiring_config = containers.WiringConfiguration(modules=["src.infrastructure.adapter.input.rest.ElementoDomandaControllers"])
    
    """ Qui indico che mi deve arrivare una dipendenza db, che sarà fornita dall'esterno """
    db = providers.Dependency()
    
    elementoDomandaContainer = providers.Container(ElementoDomandaContainer, db=db)