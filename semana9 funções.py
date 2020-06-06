import re

def le_assinatura():
    print("Bem vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio da sentença: "))
    sac = float(input("Entre a compleidade média da sentença: "))
    pal = float(input("Entre o tamanho médio da frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto" + str(i) + "(aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto" + str(i) + "(aperte enter para sair): ")
    return textos
        
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+',texto)
    if sentencas[-1] == " ":
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+',sentenca)

def separa_palavras(frase):
    return frase.split()


def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palevras_diferentes(lista_palavras):
    freqm= dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in frec:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

    
