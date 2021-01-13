ips = {}
r = 'S'
while r == 'S':
    ips[(input('Digite os dois primeiros octetos: '),
           input('Digite os dois últimos octetos: '))] = input('Nome da máquina: ')
    r = input('Digite S para continuar: ').upper()
print(ips)
for ip, nome in ips.items():
    print(f'{ip[0]}.{ip[1]}', end=' ')
    print(f'Computador: {nome}')