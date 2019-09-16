class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 33):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def Cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    miguel = Pessoa(nome='Miguel')
    Ranie = Pessoa(miguel, nome="Ranie")
    print(Pessoa.Cumprimentar(Ranie))
    print(id(Ranie))
    print(Ranie.Cumprimentar())
    print(Ranie.nome)
    print(Ranie.idade)
    for filho in Ranie.filhos:
        print(filho.nome)
    Ranie.sobrenome = 'Soares'
    del Ranie.filhos
    Ranie.olhos = 1
    Pessoa.olhos = 3
    del Ranie.olhos
    print(Ranie.__dict__)
    print(miguel.__dict__)
    print(Pessoa.olhos)
    print(Ranie.olhos)
    print(miguel.olhos)
    print(id(Pessoa.olhos), id(Ranie.olhos), id(miguel.olhos))


