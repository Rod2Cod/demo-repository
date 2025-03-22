import pytest
from src.domain import SetElementiDomanda,ElementoDomanda

elemento1 = ElementoDomanda("Qual è la capitale d'Italia?", "Roma", 1)
elemento2 = ElementoDomanda("Qual è la capitale della Francia?", "Parigi", 2)
elemento3 = ElementoDomanda("Qual è la capitale della Spagna?", "Madrid", 3)
elemento4 = ElementoDomanda("Qual è la capitale della Germania?", "Berlino", 4)
elemento5 = ElementoDomanda("Qual è la capitale del Portogallo?", "Lisbona", 5)

elementi = {elemento1, elemento2, elemento3}
newElementi = {elemento4, elemento5}
nome = "Set1"
newNome = "Set2"

class TestSetElementiDomanda:

    def setup_method(self):
        self.set_elementi_domanda = SetElementiDomanda(elementi=elementi, nome=nome)

    def test_get_elementi(self):
        """Test per il metodo getElementi."""
        assert self.set_elementi_domanda.getElementi() == elementi

    def test_get_nome(self):
        """Test per il metodo getNome."""
        assert self.set_elementi_domanda.getNome() == nome

    def test_update_elementi(self):
        """Test per il metodo updateElementi."""
        self.set_elementi_domanda.updateElementi(newElementi)
        assert self.set_elementi_domanda.getElementi() == newElementi

    def test_set_nome(self):
        """Test per il metodo setNome."""
        self.set_elementi_domanda.setNome(newNome)
        assert self.set_elementi_domanda.getNome() == newNome

    def test_domanda_associata(self):
        assert elemento1 in self.set_elementi_domanda.getElementi()