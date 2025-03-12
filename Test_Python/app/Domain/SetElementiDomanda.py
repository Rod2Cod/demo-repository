from ElementoDomanda import ElementoDomanda

class SetElementiDomanda:
    def __init__(self, elementi: set[ElementoDomanda], nome: str):
        self.__elementi = elementi
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, nome: str):
        self.__nome = nome

    def getElementiDomanda(self) -> set[ElementoDomanda]:
        return self.__elementi
    
    
    #def addElementiDomanda(self, elementi: set[int]):
    #    self.__elementi = self.__elementi.union(elementi)

    #def removeElementiDomanda(self, elementi: set[int]) -> set[ElementoDomanda]:
    #    self.__elementi = self.__elementi.difference(elementi)
    #    return self.__elementi.difference(elementi)