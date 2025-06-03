# Crie um script em Python que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.​
import json

nova_pessoa = {
    "nome": "Gabyss",
    "idade": 26,
    "cidade": "Betim"
}

def ler_arquivo_json(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        arq_json = json.loads(f.read())
        return arq_json
    
def add_json(caminho, nova_pessoa: dict):
    arq_json: list = ler_arquivo_json(caminho)    
    arq_json.append(nova_pessoa)
    print(arq_json)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(json.dumps(arq_json))
   

if __name__ == "__main__":
    # print(ler_arquivo_json("data/info-pessoas.json"))
    print(add_json("data/info-pessoas.json", nova_pessoa))