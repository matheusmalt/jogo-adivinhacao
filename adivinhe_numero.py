'''
File: adivinhacao.py
Author: Matheus Malta
Description: Jogo simples de adivinhacao
'''

import os, random, sys, math

menu = """
A-D-I-V-I-N-H-E O N-U-M-E-R-O

[1] facil 1 - 10 3 vidas
[2] médio 1 - 50 15 vidas
[3] difícil 1 - 100 30 vidas
[4] Vidente 1 - 1000 1 vidas
[5] SandBox escolha os número
[qualquer tecla] Sair
Escolha uma opção:
"""

def nucleo_jogo(menor, maior):
    try:
        randomico = random.randint(menor, maior)
        if menor == 1 and maior == 10:
            vidas = 7
        elif menor == 1 and maior == 50:
            vidas = 15
        elif menor == 1 and maior == 100:
            vidas = 30
        elif menor == 1 and maior == 1000:
            vidas = 1
        else:
            vidas = round(math.log(maior-menor + 1, 2))

        contador = vidas
        while contador > 0:
            print("Vidas: {}".format(contador))
            escolha = int(input("Digite o número: "))
            if escolha == randomico:
                print("Parabéns!!! Você acertou")
                print("O número é igual a: {}".format(escolha))
                break
            elif escolha > randomico:
                print("Tente novamente, Você chutou muito alto!")
                contador -= 1
            else:
                print("Tente novamente, você chutou muito baixo!")
                contador -= 1
            
            if contador == 0:
                print("Você perdeu :(")
                print("O número é: {}".format(randomico))
    except:
        print("Isso não é um número, tente de novo!")

def main():
    try:
        jogar_novamente = "S"
        while jogar_novamente == "S":
            os.system("clear")
            dificuldade = int(input(menu))
            if dificuldade == 1:
                nucleo_jogo(1, 10)
            elif dificuldade == 2:
                nucleo_jogo(1, 50)
            elif dificuldade == 3:
                nucleo_jogo(1, 100)
            elif dificuldade == 4:
                nucleo_jogo(1, 1000)
            else:
                try:
                    print("Escolha os números")
                    menor = int(input("Escolha o menor número: "))
                    maior = int(input("Escolha o maior número: "))
                    print("Os números escolhidos foram: {} e {}".format(menor, maior))
                    nucleo_jogo(menor, maior)
                except:
                    print("Error")
                    
            jogar_novamente = input("Deseja jogar novamente? [s][n]")
            jogar_novamente = jogar_novamente.upper()
            
    except:
        print("Saindo...")
        sys.exit()

main()
