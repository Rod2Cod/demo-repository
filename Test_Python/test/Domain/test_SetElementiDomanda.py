import pytest
from app.domain import SetElementiDomanda,ElementoDomanda

elemento1 = ElementoDomanda("Qual è la capitale d'Italia?", "Roma", 1)
elemento2 = ElementoDomanda("Qual è la capitale della Francia?", "Parigi", 2)
elemento3 = ElementoDomanda("Qual è la capitale della Spagna?", "Madrid", 3)
elemento4 = ElementoDomanda("Qual è la capitale della Germania?", "Berlino", 4)
elemento5 = ElementoDomanda("Qual è la capitale del Portogallo?", "Lisbona", 5)

elementi = {elemento1, elemento2, elemento3, elemento1}
nome = "Set1"

@pytest.fixture
def setElementi():
    return SetElementiDomanda(elementi, nome)

def test_get_elementi(setElementi):
    """Test per il metodo getElementi."""
    assert setElementi.getElementi() == elementi

def test_get_nome(setElementi):
    """Test per il metodo getNome."""
    assert setElementi.getNome() == nome

def test_update_elementi(setElementi):
    """Test per il metodo updateElementi."""
    newElementi = {elemento4, elemento5}
    setElementi.updateElementi(newElementi)
    assert setElementi.getElementi() == newElementi

def test_set_nome(setElementi):
    """Test per il metodo setNome."""
    newNome = "Set2"
    setElementi.setNome(newNome)
    assert setElementi.getNome() == newNome

def test_domanda_associata(setElementi):
    assert elemento1 in setElementi.getElementi()