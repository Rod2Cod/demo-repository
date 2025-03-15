from app.infrastructure.adapter.out.persistence.domain import ElementoDomandaEntity, SetElementiDomandaEntity, RisultatoTestEntity, RisultatoSingolaDomandaEntity

class PostgreSQLRepository:
    def __init__(self, db):
        self.db = db

    def saveElementoDomanda(self, elementoEntity: ElementoDomandaEntity) -> bool:
        try:
            self.db.session.add(elementoEntity)
            self.db.session.commit()
            return True
        except:
            return False
    
    def loadElementoDomandaById(self, idElemento: int) -> ElementoDomandaEntity:
        return ElementoDomandaEntity.query.filter_by(id=idElemento).first()
    
    def deleteElementoDomanda(self, idElemento: int) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            self.db.session.delete(elemento)
            self.db.session.commit()
            return True
        except:
            return False
    
    def loadAllElementiDomanda(self) -> set[ElementoDomandaEntity]:
        return set(ElementoDomandaEntity.query.all())
    
    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            elemento.domanda = domanda
            self.db.session.commit()
            return True
        except:
            return False
    
    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        try:
            elemento = ElementoDomandaEntity.query.filter_by(id=idElemento).first()
            elemento.risposta = risposta
            self.db.session.commit()
            return True
        except:
            return False
    
    def saveSetElementiDomanda(self, setElementiEntity: SetElementiDomandaEntity) -> bool:
        try:
            self.db.session.add(setElementiEntity)
            self.db.session.commit()
            return True
        except:
            return False
    
    def deleteSetElementiDomanda(self, nomeSet: str) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            self.db.session.delete(setElementi)
            self.db.session.commit()
            return True
        except:
            return False
    
    def loadSetElementiDomandaByNome(self, nomeSet: str) -> SetElementiDomandaEntity:
        return SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
    
    def loadAllSetElementiDomanda(self) -> set[SetElementiDomandaEntity]:
        return set(SetElementiDomandaEntity.query.all())
    
    def updateNomeSetElementiDomanda(self, nomeSet: str, nuovoNomeSet: str) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            setElementi.nome = nuovoNomeSet
            self.db.session.commit()
            return True
        except:
            return False
    
    def updateElementiSetElementiDomanda(self, nomeSet: str, elementi: set[ElementoDomandaEntity]) -> bool:
        try:
            setElementi = SetElementiDomandaEntity.query.filter_by(nome=nomeSet).first()
            setElementi.elementi = elementi
            self.db.session.commit()
            return True
        except:
            return False
    
    def saveRisultatoTest(self, risultatoTestEntity: RisultatoTestEntity) -> bool:
        try:
            self.db.session.add(risultatoTestEntity)
            self.db.session.commit()
            return True
        except:
            return False
    
    def loadRisultatoTestById(self, idRisultatoTest: int) -> RisultatoTestEntity:
        return RisultatoTestEntity.query.filter_by(id=idRisultatoTest).first()
    
    def deleteRisultatoTest(self, idRisultatoTest: int) -> bool:
        try:
            risultatoTest = RisultatoTestEntity.query.filter_by(id=idRisultatoTest).first()
            self.db.session.delete(risultatoTest)
            self.db.session.commit()
            return True
        except:
            return False
    
    def loadAllRisultatiTest(self) -> set[RisultatoTestEntity]:
        return set(RisultatoTestEntity.query.all())
    
    def loadRisultatoSingolaDomandaTestById(self, idRisultatoSingolaDomanda: int) -> RisultatoSingolaDomandaEntity:
        return RisultatoSingolaDomandaEntity.query.filter_by(id=idRisultatoSingolaDomanda).first()
    
    def loadAllRisultatiSingolaDomandaByTestId(self, idRisultatoTest: int) -> set[RisultatoSingolaDomandaEntity]:
        return set(RisultatoSingolaDomandaEntity.query.filter_by(risultato_test_id=idRisultatoTest).all())
    