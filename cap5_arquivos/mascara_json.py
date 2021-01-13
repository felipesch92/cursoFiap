import json

dicionario = {
  "chaves": ["Chaves do 8", "15/01/1995", "recep_01"],
  "quico": ["Quico Flores", "10/08/2019", "venda_02"],
  "florinda": ["Dona Florinda", "15/04/2015", "escritorio_19"]
}

with open('bd1.json', 'w') as arq_json:
    json.dump(dicionario, arq_json)
