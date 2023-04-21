#crie um programa que gere um numero e o usuario tente advinhar. O programa deve informa se chutou alto ou baixo. O usuario deverá ser capz de jogar até acerta o número
import random

#Número que o usuario tentará advinhar 
numero_aleatorio = random.randint(0, 9)

#Valor boleano para colocar no laço while, 
finalizar = True

#loop até o usuario acerta o numero
while finalizar:
    chute_usuario = int(input('Chute um número de 0 a 9: '))

    if chute_usuario > numero_aleatorio:
        print('Chutou alto!')

    elif chute_usuario < numero_aleatorio:
        print('Chutou baixo!')

    #Se o chute for igual ao número aleatorio
    else:
        print('Acertou!\nVolte sempre!')
        #Caso o usuario acerte, a variavel terá o boleano mudado para false, finalizando o laço
        finalizar = False