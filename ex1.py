
# 1. Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning.
#  Calcule a média e o desvio padrão do tempo de execução constantes. ​
from math import sqrt
import csv

media = lambda lista : sum(lista)/len(lista)
def desvio_padrão(lista):
    media_lista = media(lista)
    dp = sqrt(sum([(i - media_lista) ** 2 for i in lista])/ len(lista)) 
    return dp

def ler_arquivo(caminho):
    result = []
    with open(caminho, "r") as f:
        parse_csv = csv.reader(f)
        for i in parse_csv:
            try:
                result.append(int(i[1]))
            except:
                ...
        
    return result

if __name__ == "__main__":
    lista_log = (ler_arquivo("data/logs_treinamento.csv"))
    print(f"Média: {media(lista_log)}")
    print(f"Desvio Padrão: {desvio_padrão(lista_log)}")