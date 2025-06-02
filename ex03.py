# Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​
import csv
def ler_csv(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        csv_parseado: list = csv.reader(f)
        items = [i for i in csv_parseado]
        if not "nome" in items[0] or not "idade" in items[0] or not "cidade" in items[0]:
            print("Insira um arquivo que contenha: [nome, idade, cidade] ")
            return False

        for i in range(0, len(items)):               
            print(items[i])


if __name__ == "__main__":
    ler_csv("data/info-pessoas.csv")