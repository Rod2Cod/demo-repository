import pytest
from app.Domain import ElementoDomanda,Domanda,Risposta

@pytest.fixture
def elemento():
    return ElementoDomanda("Qual è la capitale d'Italia?", "Roma", 1)

def test_get_id(elemento):
    """Test per il metodo getId."""
    assert elemento.getId() == 1

def test_get_domanda(elemento):
    """Test per il metodo getDomanda."""
    assert elemento.getDomanda().getText() == "Qual è la capitale d'Italia?"

def test_get_risposta(elemento):
    """Test per il metodo getRisposta."""
    assert elemento.getRisposta().getText() == "Roma"

def test_set_domanda(elemento):
    """Test per il metodo setDomanda."""
    elemento.setDomanda("Qual è la capitale della Francia?")
    assert elemento.getDomanda().getText() == "Qual è la capitale della Francia?"

def test_set_risposta(elemento):
    """Test per il metodo setRisposta."""
    elemento.setRisposta("Parigi")
    assert elemento.getRisposta().getText() == "Parigi"