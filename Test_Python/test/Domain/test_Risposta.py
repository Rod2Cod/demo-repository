import pytest
from app.Domain.Risposta import Risposta

@pytest.fixture
def risposta():
    return Risposta("Roma")

def test_get_text(risposta):
    """Test per il metodo getText."""
    assert risposta.getText() == "Roma"

def test_set_text(risposta):
    """Test per il metodo setText."""
    risposta.setText("Parigi")
    assert risposta.getText() == "Parigi"