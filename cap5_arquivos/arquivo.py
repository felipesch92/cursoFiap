with open('arquivo.txt', 'w') as arq:
    arq.write('Felipe\n')
    arq.write('Tamara\n')
    arq.write('Malvo\n')

with open('arquivo.txt', 'r') as arq:
    for l in arq.readlines():
        print(f'{l}')
