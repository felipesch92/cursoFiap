from funcoes import opcao, inserir, listar, deletar
usuarios = {}
c = 1
while True:
    op = opcao()
    if op in 'IPELS':
        if op == 'I':
            inserir(usuarios, c)
            c += 1
        elif op == 'P':
            cod = int(input('Código: '))
            listar(usuarios, cod)
        elif op == 'L':
            listar(usuarios)
        elif op == 'E':
            cod = int(input('Código a ser deletado: '))
            deletar(usuarios, cod)
        else:
            break

'''usuarios[1] = ['felipe',
                        'Felipe Schmaedecke',
                        '15/10/2010',
                        'escritorio_10']
usuarios[2] = ['tamara',
                        'Tamara Cardoso Gruetzmann',
                        '04/06/1015',
                        'balcao_07']
print(usuarios)'''