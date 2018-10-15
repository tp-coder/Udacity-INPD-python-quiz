frase_facil = "Pensava-se que a Terra era __1__ ate 1492 quando Cristovao __2__ " \
              "embarcou em uma jornada para chegar as __3__ por uma rota diferente. " \
              "No entanto, ele acabou chegando na __4__. Voce sabia que os habitantes " \
              "da America foram chamados de __5__ por que Colombo achou que estava nas Indias?"
resposta_facil = ["chata", "Colombo", "Indias", "America", "indios"]
frase_medio = "sua frase medio"
resposta_medio = ["a", "b", "c", "d", "e"]
frase_dificil = "sua frase dificil"
resposta_dificil = ["f", "g", "h", "i", "j"]
frases = [frase_facil, frase_medio, frase_dificil]
respostas = [resposta_facil, resposta_medio, resposta_dificil]
chances = [3, 2, 1]
niveis = ["facil", "medio", "dificil"]


def selecionar_nivel():
    while True:
        nivel = input("Escolha facil, medio ou dificil:\n")
        if nivel in niveis:
            return nivel
        print("Nivel invalido. Tente novamente.")


def controlador_nivel():
    nivel = selecionar_nivel()
    index = niveis.index(nivel)
    jogar_nivel(frases[index], respostas[index], chances[index])


def jogar_nivel(frase, lista_respostas, num_chances):
    print('\n' + frase + '\n')
    print(lista_respostas)
    print("")
    print(str(num_chances) + '\n')


controlador_nivel()
