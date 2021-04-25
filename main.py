"""
Laços em Python tem suporte a uma clausula ELSE.
Isso significa que após o término de um iteravel, se nenhuma condicao for atendida a contento,
voce pode executar uma nova instrucao. Como se fosse um finnaly.

e.g

"""

def contem(palheiro, agulha):
    #iremos criar um erro se nao encontrarmos a agulha no palheiro
    for item in palheiro:
        if item == agulha:
            print("Achei a agulha no palheiro")
            break
    else:
        #esse else só será executado se o for acima, nao bater no break nenhuma vez.
        raise ValueError("A Agulha não foi encontrada")

"""
Honestamente, esse é um recurso interessante, mas que por nao se assemelhar a muitas outras 
linguagens, acaba gerando confusao quando vemos códigos reais. 

uma solucao mais LEGIVEL para esse problema de apresentar algo quando um loop nunca atingir algo,
seria utilizarmos uma abordagem como: 
"""

def contem_melhor(palheiro, agulha):
    for item in palheiro:
        if item == agulha:
            print("achei a agulha")
    raise ValueError("A agulha não foi encontrada")

"""
Agora... se for pra deixar o Guido(criador do python feliz), sempre podemos deixar
mais pythonico escrevendo um esquema tipo... 
"""

def contem_pythonico(palheiro, agulha):
    for item in palheiro:
        if agulha not in palheiro:
            raise ValueError("Agulha não encontrada")
        else:
            print("ta aqui a agulha")

if __name__ == "__main__":
    #contem([23,"agulha",0xbadc0ffee],"agulha")
    #contem([23, "aaa", 0xbadc0ffee], "agulha")
    #contem_melhor([23,"agulha",0xbadc0ffee],"agulha")
    contem_pythonico([23,"22",0xbadc0ffee],"agulha")