from app.infrastructure.adapter.out.persistence.Extensions import db

class RisultatoSingolaDomandaEntity(db.Model):
    __tablename__ = 'risultato_singola_domanda'
    id = db.Column(db.Integer, primary_key=True)  # Chiave primaria
    domanda = db.Column(db.Text, nullable=False)
    risposta = db.Column(db.Text, nullable=False) 
    rispostaLLM = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, nullable=False)
    metrica1 = db.Column(db.Float, nullable=False)
    metrica2 = db.Column(db.Float, nullable=False)
    metrica3 = db.Column(db.Float, nullable=False)
    metrica4 = db.Column(db.Float, nullable=False)
    metrica5 = db.Column(db.Float, nullable=False)
    metrica6 = db.Column(db.Float, nullable=False)
    risultatoTestId = db.Column(db.Integer, db.ForeignKey('risultato_test.id', ondelete='CASCADE'), nullable=False)
    

class RisultatoTestEntity(db.Model):
    __tablename__ = 'risultato_test'
    id = db.Column(db.Integer, primary_key=True)  # Chiave primaria
    data = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.Float, nullable=False)
    nomeSet = db.Column(db.Text, nullable=True)
    risultati = db.relationship('RisultatoSingolaDomandaEntity', backref="risultato_test", nullable=False)  # Relazione uno a molti con la tabella risultato_singola_domanda (bidirezionale)