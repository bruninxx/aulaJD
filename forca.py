import random
def jogar() :
    sorteio_palavra_int = random.randint(1,3)
    print("###### Bem vindo ao jogo da FORCA ######")
    if sorteio_palavra_int == 1:
        palavra_secreta = "estrela"
    elif sorteio_palavra_int == 2:
        palavra_secreta = "cafe"
    elif sorteio_palavra_int == 3:
        palavra_secreta = "balacobaco"
        elif sorteio_palavra_int == 4:
        palavra_secreta = "avengers"
        elif sorteio_palavra_int == 5:
        palavra_secreta = "processador"
        elif sorteio_palavra_int == 6:
        palavra_secreta = "balança"
        elif sorteio_palavra_int == 7:
        palavra_secreta = "refrigerante"
        elif sorteio_palavra_int == 8:
        palavra_secreta = "teclado"
        elif sorteio_palavra_int == 9:
        palavra_secreta = "caderno"
        elif sorteio_palavra_int == 10:
        palavra_secreta = "mouse"

    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")
    #letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False
    erros=0
    
    while(not acertou and not enforcou):
        print(letras_acertadas)
        chute = input("Digite a letra\n")

        print("Você digitou", chute)
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Letra '{}' encontrada na posição {}".format(chute,index))
                letras_acertadas[index] = chute            
            index = index + 1

        if letras_acertadas.count("_") == 0:
            acertou = True
            print("Parabéns, você acertou a palavra!")
        
    ## PROGRAMAÇÃO CRIADA
    print("##### FIM DO JOGO #####")


if (__name__ == '__main__'):
    jogar()