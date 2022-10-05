from marvel_viloes import MarvelViloes


class ViloesSentimentaisMarvel:
    def setup_class(self):
        self.vilao_1 = MarvelViloes("Super Fofoqueiro", ["Espalhar mentiras'"], 4)
        self.vilao_2 = MarvelViloes('agronomo do tio luci', ['plantar discordia'], 2 )
        self.vilao_3 = MarvelViloes('Super Ego', ['antipatia'], 5)
   
    def test_primeiro_vilao(self):
        self.vilao_1.set_nome('Super Fofoqueiro') 
        assert self.vilao_1.get_nome() == 'Super Fofoqueiro'
        assert self.vilao_1.set_nome({}) == 'Somente escrita'

    def test_segundo_vilao(self):
        self.vilao_2.set_nome('agronomo do tio luci')
        assert self.vilao_2.get_nome() == 'agronomo do tio luci'
        assert self.vilao_2.set_nome([]) == 'Somente escrita'
    
    def test_terceiro_vilao(self):
        self.vilao_3.set_nome('Super Ego')
        assert self.vilao_3.get_nome() == 'Super Ego'
        assert self.vilao_3.set_nome(1234) == 'Somente escrita'

    def test_poderes(self):
        self.vilao_1.set_poderes(['Espalhar mentiras'])
        assert self.vilao_1.get_poderes() == (['Espalhar mentiras'])
        assert self.vilao_1.set_poderes(12345678) == 'O formato de entrada é de lista'

        self.vilao_2.set_poderes(['plantar discordia'])
        assert self.vilao_2.get_poderes() == (['plantar discordia'])
        assert self.vilao_2.set_poderes(("str")) == 'O formato de entrada é de lista'

        self.vilao_3.set_poderes(['antipatia'])
        assert self.vilao_3.get_poderes() == (['antipatia'])
        assert self.vilao_3.set_poderes(("None")) == 'O formato de entrada é de lista'

    def test_perigo(self):
        self.vilao_1.set_perigo(4)
        assert self.vilao_1.get_perigo() == (4)
        assert self.vilao_1.set_perigo(-3) == 'O nivel de Perigo vai de 0 ao 5'

        self.vilao_2.set_perigo(5)
        assert self.vilao_2.get_perigo() == (5)
        assert self.vilao_2.set_perigo(10) == 'O nivel de Perigo vai de 0 ao 5'

        self.vilao_3.set_perigo(1)
        assert self.vilao_3.get_perigo() == (1)
        assert self.vilao_3.set_perigo(6) == 'O nivel de Perigo vai de 0 ao 5'
    
    def test_dominar_mundo(self):
        assert self.vilao_1.dominar_mundo() == 'Vilão Preso'
        assert self.vilao_2.dominar_mundo() == 'Vilão morto'
        assert self.vilao_3.dominar_mundo() == 'VILÃO DOMINOU O  MUNDO'