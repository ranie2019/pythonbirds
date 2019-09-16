class Pessoa:
    def __init__(self, nome = None, idade = 33):
        self.nome = None

    def Cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('joao')
    print(Pessoa.Cumprimentar(p))
    print(id(p))
    print(p.Cumprimentar())
    print(p.nome)
    p.nome = 'Ranie'
    print(p.nome)
    print(p.idade)

