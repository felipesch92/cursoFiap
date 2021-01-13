import json
from uteis import verifica
inventario = {}
op = int(input('[1] Registrar ativo [2] Exibir ativos '))
while op < 3 and op > 0:
    if op == 1:
        r = 'S'
        while r == 'S':
            while True:
                n_patrimonio = input('Número patrimonio:')
                with open('inventario.json') as arq_json:
                    dic_json = json.load(arq_json)
                    if n_patrimonio in dic_json:
                        print('Número já existe, digite outro.')
                    else:
                        break
            inventario[n_patrimonio] = [
                        input('Descrição: '),
                        input('Departamento: ')]
            r = input('Continuar? ').upper()
        with open('inventario.json', 'r+') as arq_json:
            dado = json.load(arq_json)
            dado.update(inventario)
            arq_json.seek(0)
            json.dump(dado, arq_json)
        print('JSON gerado!')
    elif op == 2:
        with open('inventario.json', 'r') as arq_json:
            res = json.load(arq_json)
            for c, d in res.items():
                print(f'Número Patrimonio: {c}')
                print(f'Descrição: {d[0]}')
                print(f'Departamento: {d[1]}')
                print('-' * 40)
    op = int(input('[1] Registrar ativo [2] Exibir ativos '))