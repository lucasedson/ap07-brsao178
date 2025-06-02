# 2. Crie um script em Python que escreva dados em um arquivo CSV.
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​
import csv
info = [
    ["nome", "idade", "cidade"],
    ["Lucas", "28", "Cabo Frio"],
    ["Moises", "26", "Nárnia"]
]

def escreve_csv(lista_info):
    try:
        with open("data/info-pessoas.csv", "w", newline='', encoding="utf-8") as f:
            escritor = csv.writer(f)
            for i in range(0, len(lista_info)):
                escritor.writerow(lista_info[i])
        print("Arquivo salvo com sucesso.")
    except:
        print("Houve algum erro.")
    

if __name__ == "__main__":
    escreve_csv(info)