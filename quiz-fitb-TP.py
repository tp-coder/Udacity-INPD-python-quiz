"""
Este programa eh um jogo tipo "fill in the blanks".
Eh um dos requisitos para concluir o Nanogegree Introducao a programacao da Udacity.
"""

# texto do modo facil
texto_facil = """Pensava-se que a Terra era __1__. ate 1492 quando Cristovao __2__ embarcou em uma jornada para chegar as __3__ por uma rota diferente. No entanto, ele acabou chegando na __4__.
Voce sabia que os habitantes da America foram chamados de __5__ por que Colombo achou que estava nas Indias?""" 
# lista com as respostas do modo facil
lista_resp_facil = ["chata", "Colombo", "Indias", "America", "indios"]
# lista com os elementos do texto que deverao ser fornecidos pelo jogador
lista_busca_palavras_facil = ["__1__", "__2__", "__3__", "__4__", "__5__",]

'''
def escolha_dificuldade(dificuldade, texto, lista_resp, lista_busca_palavras, num_tentativas):
    if dificuldade == "facil" or dificuldade == "Facil" or dificuldade == "FACIL":
        print("Voce escolheu o modo facil! Divirta-se!")
        print("")
        modo_facil(texto_facil, lista_resp_facil, lista_busca_palavras_facil, num_tentativas)
    if dificuldade == "media" or dificuldade == "Media" or dificuldade == "MEDIA":
        print("Voce escolher o modo medio. Seu conhecimento sera testado!")
        print("")
    if dificuldade == "dificil" or dificuldade == "Dificil" or dificuldade == "DIFICIL":
        print("Voce optou pelo modo dificil; Voce nao sobrevivera! :D")
        print("")
'''
def modo_facil(texto_facil, lista_resp_facil, lista_busca_palavras_facil, num_tentativas):
    # funcao para o jogo modo facil
    # imprime para o jogador o texto facil
    print('\n' + texto_facil + '\n')
    # metodo para transformar o texto numa lista
    texto_facil = texto_facil.split()
    substitui_palavra = []
    #for palavra in texto_facil:
    for palavra in texto_facil:
        troca_palavra = busca_palavras('facil', palavra, lista_busca_palavras_facil)
        if troca_palavra != None:
            # palavra = palavra.replace(testa_palavra, "MUDADO")
            palavra = palavra.replace(palavra, troca_palavra)
            substitui_palavra.append(palavra)
        else:
            substitui_palavra.append(palavra)
    texto_final = " ".join(substitui_palavra)
    print(texto_final)
    return texto_final
            
def busca_palavras(modo, palavra_buscada, lista_busca_palavras):
    if modo == "facil":
        for elemento in lista_busca_palavras:
            if elemento in palavra_buscada:
                palavra_resposta = valida_palavra('facil', lista_resposta=lista_resp_facil, num_tentativas=tentativas, elemento=elemento)
                return palavra_resposta
        return None

def valida_palavra(modo, lista_resposta, num_tentativas, elemento):
    tentativas = 0
    if modo == 'facil':
        while tentativas < num_tentativas:
            palavra_resposta = input("Qual a resposta para " + elemento + "\n")
            if palavra_resposta in lista_resposta:
                print("Boa, voce acertou!!\n")
                return palavra_resposta
            else:
                print("Acho que essa nao eh a resposta certa \n")
                tentativas += 1
        return 'Game over!'

# Programa principal
print("""Ola! Vamos jogar o "fill in the blanks".

O jogo eh assim: voce vera uma frase com espacos numerados que deverao ser preenchidos com a resposta correta. Por exemplo: O animal mais bonitinho do planeta eh o __1__, que adora receber carinho.
Voce deve responder o animal certo, no caso o gato. Se voce acertar, ira para a proxima palavra; se errar tentara acertar uma quantidade X de vezes ate acertar ou o jogo terminar.

Entao vamos comecar!
Ah, nao use acentuacao, beleza?!
""")
# variavel para armazenar qtas vezes o jogador tentara descobrir a palavra ate o jogo terminar.
tentativas = input("Quantas vezes voce gostaria de tentar descobrir a palavra?\n")
'''
# teste se a variavel tentativas eh um numero inteiro
while True:
    try:
        int(tentativas)
    except ValueError:
        tentativas = input("Por favor, escolha um numero :)\n")
'''
# variavel para o usuario escolher a dificuldade do jogo.
dificuldade_jogo = input("Agora escolha a dificuldade do jogo. As opcoes sao facil, medio ou dificil:\n")

# O programa usara a escolha do usuario para direciona-lo ao texto certo.

if dificuldade_jogo == "facil" or dificuldade_jogo == "Facil" or dificuldade_jogo == "FACIL":
    modo_facil(texto_facil, lista_resp_facil, lista_busca_palavras_facil, tentativas)

#tentativas = 3
#print(modo_facil(texto_facil,lista_resp_facil,lista_busca_palavras_facil, tentativas))