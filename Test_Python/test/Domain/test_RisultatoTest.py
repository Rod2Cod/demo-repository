import pytest
from app.domain import RisultatoTest, RisultatoSingolaDomanda

# TEST RISULTATO SINGOLA DOMANDA

id = 1
domanda = "Qual è la capitale d'Italia?"
risposta = "Roma"
rispostaLLM = "Roma"
score = 1.0
metriche = {"metrica1": 0.5, "metrica2": 0.5}

@pytest.fixture
def risultato_singola_domanda():
    return RisultatoSingolaDomanda(id, domanda, risposta, rispostaLLM, score, metriche)

def test_get_id_risultatoSingolaDomanda(risultato_singola_domanda):
    """Test per il metodo getId."""
    assert risultato_singola_domanda.getId() == id

def test_get_domanda(risultato_singola_domanda):
    """Test per il metodo getDomanda."""
    assert risultato_singola_domanda.getDomanda() == domanda

def test_get_risposta(risultato_singola_domanda):
    """Test per il metodo getRisposta."""
    assert risultato_singola_domanda.getRisposta() == risposta

def test_get_risposta_llm(risultato_singola_domanda):
    """Test per il metodo getRispostaLLM."""
    assert risultato_singola_domanda.getRispostaLLM() == rispostaLLM

def test_get_scoreRisultatoSingolaDomanda(risultato_singola_domanda):
    """Test per il metodo getScore."""
    assert risultato_singola_domanda.getScore() == score

def test_get_metriche(risultato_singola_domanda):
    """Test per il metodo getMetriche."""
    assert risultato_singola_domanda.getMetriche() == metriche

# TEST RISULTATO TEST

risultato_singola_domanda1 = RisultatoSingolaDomanda(id, domanda, risposta, rispostaLLM, score, metriche)
risultato_singola_domanda2 = RisultatoSingolaDomanda(2, "Qual è la capitale della Francia?", "Parigi", "Parigi", 1.0, {"metrica1": 0.5, "metrica2": 0.5})
risultato_singola_domanda3 = RisultatoSingolaDomanda(3, "Qual è la capitale della Spagna?", "Madrid", "Madrid", 1.0, {"metrica1": 0.5, "metrica2": 0.5})
risultato_singola_domanda4 = RisultatoSingolaDomanda(4, "Qual è la capitale della Germania?", "Berlino", "Berlino", 1.0, {"metrica1": 0.5, "metrica2": 0.5})

id = 1
scoreGenerale = 1.0
LLM = "ChatGPT"
dataEsecuzione = "2025-03-13"
nomeSet = "Set1"
risultatiDomande = {risultato_singola_domanda1, risultato_singola_domanda2, risultato_singola_domanda3, risultato_singola_domanda4}

@pytest.fixture
def risultato_test():
    return RisultatoTest(id, scoreGenerale, LLM, dataEsecuzione, nomeSet, risultatiDomande)

def test_get_id(risultato_test):
    """Test per il metodo getId."""
    assert risultato_test.getId() == id

def test_get_score(risultato_test):
    """Test per il metodo getScore."""
    assert risultato_test.getScore() == score

def test_get_LLM(risultato_test):
    """Test per il metodo getLLM."""
    assert risultato_test.getLLM() == LLM

def test_get_data_esecuzione(risultato_test):
    """Test per il metodo getDataEsecuzione."""
    assert risultato_test.getDataEsecuzione() == dataEsecuzione

def test_get_nome_set(risultato_test):
    """Test per il metodo getNomeSet."""
    assert risultato_test.getNomeSet() == nomeSet

def test_get_risultati_domande(risultato_test):
    """Test per il metodo getRisultatiDomande."""
    assert risultato_test.getRisultatiDomande() == risultatiDomande