base_dados = []
with open('iris.data', 'r') as arq:
    for reg in arq.readlines():
        base_dados.append(reg.split(','))

print(base_dados)

print(float(base_dados[0][0]) + float(base_dados[0][1]))
