class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome: str = None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ol￿á, meu nome ￿é {self.nome}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos} - '


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_pai = super().cumprimentar() #Super chama a classe Pai.
        return f'{cumprimentar_pai} Aperto de mao'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    anonimo = Homem(nome='anonimo')
    mutante = Mutante(nome='Mutante')
    felipe = Pessoa(anonimo, nome="Felipe", idade=31)
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    print(felipe.idade)
    for f in felipe.filhos:
        print(f.nome)
    felipe.sobrenome = "Iasi"
    print(felipe.sobrenome)
    print(felipe.__dict__)
    print(felipe.olhos)
    print(Pessoa.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), felipe.nome_e_atributos_de_classe())
    print(isinstance(anonimo, Pessoa))
    print(felipe.olhos)
    print(mutante.olhos)
    print(mutante.cumprimentar())
    print(felipe.cumprimentar())
    print(anonimo.cumprimentar())
