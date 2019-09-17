"""
voce deve criar uma classe carro que vai possuir atributos compostos
por outas duas classes:

 1) motor
 2) direcao

 o motor tera a responsabilidade de controlar a  velocidade.
 ele oferece os seguintes atibutos:

 1) atributo dados de velocidades
 2) metodo acelerar, que deverar incrementar a velocidade de uma unidade
 3) metodo frear que deverar decrementrar a velocidade em duas unidades

 a direcao tera a responsabilidade de controlar a direcao  ela oferece os seguintes
 atributos

 1) valores de direcao com valores possiveis: norte, sul, leste, oeste.
 2) metodo girar a direcao
 3) metodo girar a esquerda

   N
 O   L
   S

   exemplo:
   >>> # testando motor
   >>> motor = motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   >>> #testando direcao
   >>> direcao = direcao()
   >>> direcao = valor
   'norte'
   >>> direcao = girar_a_direita()
   >>> direcao = valor
   'leste'
   >>> direcao = girar_a_direita()
   >>> direcao = valor
   'sul'
   >>> direcao = girar_a_direita()
   >>> direcao = valor
   'oeste'
   >>> direcao = girar_a_direita()
   >>> direcao = valor
   'norte'
   >>> direcao = girar_a_esquerad()
   >>> direcao = valor
   'oeste'
   >>> direcao = girar_a_esquerad()
   >>> direcao = valor
   'sul'
   >>> direcao = girar_a_esquerad()
   >>> direcao = valor
   'leste'
   >>> direcao = girar_a_esquerad()
   >>> direcao = valor
   'norte'
   >>> carro = carro(direcao, motor)
   >>> carro.calcular_velocidade()
   0
   >>> carro = acelerar()
   >>> carro.calcular_velocidade()
   1
   >>> carro = acelerar()
   >>> carro.calcular_velocidade()
   2
   >>> carro = frear()
   >>> carro.calcular_velocidade()
   0
   >>> carro.calcular.direcao()
   >>> 'norte'
   >>> carro.girar_a_direira()
   >>> carro.calcular_direcao()
   >>> 'leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   >>> 'norte'
    >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   >>> 'oeste'

"""
NORTE= 'norte'
SUL= 'sul'
LESTE= 'leste'
OESTE= 'oeste'

class motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class direcao:
    rotacao_a_direita_dct={NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct={NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __int__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
            self.valor = self.rotacao_a_esquerda_dct[self.valor]