def opcao():
    op = input('O que deseja realizar? '
               '[I] - Inserir usuário - '
               '[P] - Pesquisar usuário - '
               '[E] - Excluir usuário - '
               '[L] - Listar usuário'
               '[S] - Sair').upper()
    return op


def inserir(usuarios, cod):
    usuarios[cod] = [input('Informe o login: ').upper(),
                       input('Nome: ').upper(),
                       input('Informe a última data de acesso: '),
                       input('Informe a última estação acessada: ').upper()]
    salvar(usuarios)

def listar(usuarios, cod=0):
    if cod != 0:
        if usuarios.get(cod):
            u = usuarios.get(cod)
            print(f'Código: {cod}')
            print(f'Login: {u[0]}')
            print(f'Usuário: {u[1]}')
            print(f'Último acesso: {u[2]}')
            print(f'Última estação: {u[3]}')
        else:
            print('Login não encontrado!')
    else:
        for c, u in usuarios.items():
            print(f'Código: {c}')
            print(f'Login: {u[0]}')
            print(f'Usuário: {u[1]}')
            print(f'Último acesso: {u[2]}')
            print(f'Última estação: {u[3]}')
            print('-' * 40)


def deletar(usuarios, u):
    if usuarios.get(u):
        del usuarios[u]
        print(f'O Código {u} foi deletado com sucesso!')
    else:
        print('Código não encontrado.')


def salvar(dicionario):
    with open('bd.txt', 'a') as arquivo:
        for c, v in dicionario.items():
            arquivo.write(f'{c}:{v}')
