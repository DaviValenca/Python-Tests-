#Crie uma classe que modele uma pessoa e permita definir e obter a idade, peso
#e altura da pessoa e que permita fazer a pessoa envelhecer, engordar e
#emagrecer. A cada ano que a pessoa envelhece, sendo a idade dela menor que
#21 anos, ela deve crescer 1,5 cm
class Pessoa:
    def __init__(self, idade, peso, altura):
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,envelheceu):
        self.idade += envelheceu
        if envelheceu < 22:
            self.adicionarcm(self.altura+1.5*envelheceu)
        
    def adicionarcm(self, altura):
        self.altura = altura

    def emagrecer(self, emagreceu):
        self.peso -= emagreceu

    def engordar(self, engordou):
        self.peso += engordou

