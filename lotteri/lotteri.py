import random

class lotteri:

    def __init__(self):

        self.list_vinster = {
            "Kruka",
            "Fot massage från Amin",
            "Strumpa med hål",
            "Trasig ballong",
            "Fri entre på soptippen",
            "En ruta marabou choklad",
            "En ofungerande whiteboard tavla",
            "Sten från 1700-talet",
            "Date med Emil",
            "Slaskig gurka"
        }

    
    def get_vinst(self):
        slumptal = random.randint(0, len(self.list_vinster)-1 )

        return self.list_vinster[slumptal]
