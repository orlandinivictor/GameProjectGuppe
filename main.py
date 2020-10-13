import random
print('Bem-vindo ao Quizz Guppe!')
print('Teste seus conhecimentos matemáticos!!!')
print('versão 0.0.1')
pontos = 0
while True:
    print('Escolha a sua dificuldade')
    dificuldade = int(input('1- Fácil, 2- Médio, 3- Dificil, 0- Sair: '))
    if dificuldade == 0:
        break
    else:
        while True:
            if dificuldade == 1:
                num1 = random.randint(0, 10)
                num2 = random.randint(0, 10)
                operacao = random.randint(0, 2)
                if operacao == 1:
                    resultado = num1 + num2
                    resposta = int(input(f'Quanto é {num1} + {num2}? '))
                    if resposta == resultado:
                        pontos += 1
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 2:
                    resultado = num1 - num2
                    resposta = int(input(f'Quanto é {num1} - {num2}? '))
                    if resposta == resultado:
                        pontos += 1
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 0:
                    resultado = num1 * num2
                    resposta = int(input(f'Quanto é {num1} * {num2}? '))
                    if resposta == resultado:
                        pontos += 1
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
            elif dificuldade == 2:
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)
                operacao = random.randint(0, 2)
                if operacao == 1:
                    resultado = num1 + num2
                    resposta = int(input(f'Quanto é {num1} + {num2}? '))
                    if resposta == resultado:
                        pontos += 2
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 2:
                    resultado = num1 - num2
                    resposta = int(input(f'Quanto é {num1} - {num2}? '))
                    if resposta == resultado:
                        pontos += 2
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 0:
                    resultado = num1 * num2
                    resposta = int(input(f'Quanto é {num1} * {num2}? '))
                    if resposta == resultado:
                        pontos += 2
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
            elif dificuldade == 3:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacao = random.randint(0, 2)
                if operacao == 1:
                    resultado = num1 + num2
                    resposta = int(input(f'Quanto é {num1} + {num2}? '))
                    if resposta == resultado:
                        pontos += 3
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 2:
                    resultado = num1 - num2
                    resposta = int(input(f'Quanto é {num1} - {num2}? '))
                    if resposta == resultado:
                        pontos += 3
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
                elif operacao == 0:
                    resultado = num1 * num2
                    resposta = int(input(f'Quanto é {num1} * {num2}? '))
                    if resposta == resultado:
                        pontos += 3
                        print(f'Parabéns, você acertou, e agora você tem {pontos} pontos.')
                    else:
                        print(f'Você errou e tem {pontos} pontos.')
            else:
                print('Dificuldade Inválida, escolha novamente.')
                break
            print('Gostaria de continuar jogando?')
            kplay = input('Y - sim / N - nao: ')
            if kplay.upper() == 'N':
                break
            elif kplay.upper() == 'Y':
                pass
            else:
                print('Escolha inválida')
