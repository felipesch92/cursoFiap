import json

def verifica(pat):
    with open('inventario.json', 'r') as arq_json:
        dic_json = json.load(arq_json)
        print(dic_json)
        if pat in dic_json:
            print('Número já existe')
        else:
            print('Número não existe')
