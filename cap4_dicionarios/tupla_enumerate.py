usuarios = {}
r = 'S'
emails = []
while r == 'S':
    emails.append(input('E-mail: ').lower())
    r = input('Digite S para continuar.').upper()
tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print(f'Email: {tupla[chave][1]}')
    usuarios[tupla[chave]] = [input('Digite o nome'), input('Digite o nível')]
print(usuarios)