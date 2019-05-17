#Por Milton Gonçalves Junior
#Usei o pycharm,
#_*_coding: utf-8 _*_
#biblioteca que usei foi a statiscs as s , com s.harmonic_mean
import statistics as s
#interação com o usuário .
nome = input('Olá qual é o seu nome?:')
print('Seja Bem-vindo!','\033[5;32m',nome,'\33[m')
print('===================================')
print('\n\n','\033[5;33m'
'Seu veículo realizou o trajeto de velocidade'
'\n Entre as cidades A, B e a volta.'
'\n Qual a velocidade média que você realizou todo o percurso,'
'\n De cidade A, cidade B e volta?'
'\n Vamos lá? insira os 3 valores '
'\n e obtenha seu resultado.\n\n')
x1 = int(input('Na cidade A sua velocidade foi quanto?'))
print(x1,'km')
x2 = int(input('Na cidade B sua velocidade foi quanto?'))
print(x2,'km')
x3 = int(input('Na volta?'))
print(x3,'km')
print ('\n',nome,'. A velocidade média que você realizou todo o percurso Foi \n')
lista = [int(x1), int(x2), int(x3)]
#resultado….
resultado = s.harmonic_mean(lista)
print(resultado,'km')
#bibliografia:cursoemvidio.com
