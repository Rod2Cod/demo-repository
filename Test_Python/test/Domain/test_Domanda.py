import pytest
from app.Domain.Domanda import Domanda

@pytest.fixture
def domanda():
    return Domanda("Qual è la capitale d'Italia?")

def test_get_text(domanda):
    """Test per il metodo getText."""
    assert domanda.getText() == "Qual è la capitale d'Italia?"

def test_set_text(domanda):
    """Test per il metodo setText."""
    domanda.setText("Qual è la capitale della Francia?")
    assert domanda.getText() == "Qual è la capitale della Francia?"