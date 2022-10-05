class MarvelViloes: 
    def __init__(self, nome: str, poderes: list, perigo: int) -> None:
        self.nome = nome 
        self.poderes = poderes
        self.perigo = perigo

    def get_nome(self, nome):
        return self.nome

    def set_nome(self, nome):
        if type(nome) != str:
            return ("Somente escrita")

        self.nome = nome

    def get_poderes(self, poderes):
        return self.poderes

    def set_poderes(self, poderes):
        if type(poderes) != list:
            return ("O formato de entrada é de lista")     

        self.poderes = poderes

    def get_perigo(self, perigo):
        return self.perigo

    def set_perigo(self, perigo):
        if perigo >= 0 and perigo <= 5:
                self.perigo = perigo

        return ("O nivel de Perigo vai de 0 ao 5")

    def dominiar_mundo(self,perigo):
        if perigo <= 2:
            return "Vilão morto"

        elif perigo > 2 and perigo <= 4:
            return "Vilão Preso"

        else:
            return "VILÃO DOMINOU O MUNDO"

