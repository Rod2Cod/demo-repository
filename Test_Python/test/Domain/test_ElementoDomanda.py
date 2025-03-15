import pytest
from app.domain import ElementoDomanda,Domanda,Risposta

# TEST DOMANDA

domanda = "Qual è la capitale d'Italia?"

@pytest.fixture
def domanda_fixture():
    return Domanda(domanda)

def test_get_text(domanda_fixture):  
    """Test per il metodo getText."""
    assert domanda_fixture.getText() == domanda

def test_set_text(domanda_fixture):
    """Test per il metodo setText."""
    domanda_fixture.setText("Qual è la capitale della Francia?")
    assert domanda_fixture.getText() == "Qual è la capitale della Francia?"

# TEST RISPOSTA

risposta = "Roma"

@pytest.fixture
def risposta_fixture():
    return Risposta(risposta)

def test_get_text(risposta_fixture):
    """Test per il metodo getText."""
    assert risposta_fixture.getText() == risposta

def test_set_text(risposta_fixture):
    """Test per il metodo setText."""
    risposta_fixture.setText("Parigi")
    assert risposta_fixture.getText() == "Parigi"

# TEST ELEMENTO DOMANDA

id = 1

@pytest.fixture
def elemento():
    return ElementoDomanda(domanda, risposta, id)

def test_get_id(elemento):
    """Test per il metodo getId."""
    assert elemento.getId() == id

def test_get_domanda(elemento):
    """Test per il metodo getDomanda."""
    assert elemento.getDomanda().getText() == domanda

def test_get_risposta(elemento):
    """Test per il metodo getRisposta."""
    assert elemento.getRisposta().getText() == risposta

def test_set_domanda(elemento):
    """Test per il metodo setDomanda."""
    newTextDomanda = "Qual è la capitale della Francia?"
    elemento.setDomanda(newTextDomanda)
    assert elemento.getDomanda().getText() == newTextDomanda

def test_set_risposta(elemento):
    """Test per il metodo setRisposta."""
    newTextRisposta = "Parigi"
    elemento.setRisposta(newTextRisposta)
    assert elemento.getRisposta().getText() == newTextRisposta