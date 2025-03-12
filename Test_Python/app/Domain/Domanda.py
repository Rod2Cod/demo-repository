class Domanda:
    def __init__(self, text: str):
        self.__text = text

    def getText(self) -> str:
        return self.__text
    
    def setText(self, text: str):
        self.__text = text