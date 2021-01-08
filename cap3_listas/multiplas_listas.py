equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número serial: ')))
    departamentos.append(input('Departamento: '))
    resposta=input('Digite \'S\' para continuar: ').upper()

for i in range(0, len(equipamentos)):
    print(f'Cod {i}', end=' ')
    print(f'Equipamento: {equipamentos[i]}', end=' ')
    print(f'Valor: {valores[i]}', end=' ')
    print(f'Serial: {seriais[i]}', end=' ')
    print(f'Departamento: {departamentos[i]}')
    print('-' * 30)

'''busca = input('Informe o nome do equipamento que deseja buscar: ')
for i in range(0, len(equipamentos)):
    if busca == equipamentos[i]:
        print(f'Cod {i}', end=' ')
        print(f'Equipamento: {equipamentos[i]}', end=' ')
        print(f'Valor: {valores[i]}', end=' ')
        print(f'Serial: {seriais[i]}', end=' ')
        print(f'Departamento: {departamentos[i]}')
        print('-' * 30)
for i in range(0, len(equipamentos)):
    if equipamentos[i] == 'Impressora':
        valores[i] = valores[i] * 0.9
    print(f'{equipamentos[i]} {valores[i]}')'''
excluir = int(input('Informe o serial que será excluido: '))
for i in range(0, len(equipamentos)):
    if seriais[i] == excluir:
        del equipamentos[i]
        del valores[i]
        del seriais[i]
        del departamentos[i]

for i in range(0, len(equipamentos)):
    print(f'Cod {i}', end=' ')
    print(f'Equipamento: {equipamentos[i]}', end=' ')
    print(f'Valor: {valores[i]}', end=' ')
    print(f'Serial: {seriais[i]}', end=' ')
    print(f'Departamento: {departamentos[i]}')
    print('-' * 30)

# CAP 3 até a página 14