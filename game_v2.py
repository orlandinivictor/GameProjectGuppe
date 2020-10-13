import random
print(''.center(41, '-'))
print('Bem-vindo ao Quizz Guppe!'.center(41, '-'))
print(''.center(41, '-'))
print('Teste seus conhecimentos matemáticos!!!'.center(41, '-'))
print('versão 0.0.2'.center(41, '-'))
print(''.center(41, '-'))


def multiplicar(a, b):
    return a * b


def subtrair(a, b):
    return a - b


def somar(a, b):
    return a + b


class Jogo:

    pontos = 0

    def __init__(self):
        print('Escolha sua Dificuldade: ')
        while True:
            self.dif = input('1- Fácil, 2- Médio, 3- Dificil, 0- Sair: ')
            if [letra for letra in self.dif if letra in '0123456789-']:
                break
            else:
                print('Dificuldade deve ser um número inteiro.')
        self.dif = int(self.dif)
        self.num1 = random.randint(0, (10 ** self.dif))
        self.num2 = random.randint(0, (10 ** self.dif))
        self.op = None

    def jogar(self):
        resposta = Jogo.operacao(self)
        while True:
            teste = input(f'Quanto é {self.num1}{self.op}{self.num2}? ')
            if [letra for letra in teste if letra in '0123456789-']:
                break
            else:
                print('A resposta deve ser um número inteiro.')
        teste = int(teste)
        if resposta == teste:
            Jogo.pontos += self.dif
            print(f'Você acertou! Seu saldo é de {Jogo.pontos} pontos.')
        else:
            print(f'Você errou. Seu saldo é de {Jogo.pontos} pontos.')

    def operacao(self):
        x = random.randint(0, 2)
        if x == 0:
            self.op = '+'
            return somar(self.num1, self.num2)
        elif x == 1:
            self.op = '-'
            return subtrair(self.num1, self.num2)
        elif x == 2:
            self.op = '*'
            return multiplicar(self.num1, self.num2)


while True:
    joga = Jogo()
    if joga.dif == 0:
        print(f'Você terminou o jogo com {Jogo.pontos} pontos.')
        print('Fechando o jogo!')
        break
    elif joga.dif == 1 or joga.dif == 2 or joga.dif == 3:
        joga.jogar()
    else:
        print('Escolha deve ser entre 0 e 3, tente novamente!')
