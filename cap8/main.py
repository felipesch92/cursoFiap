emails = []
emails[0] = 'felipe@sicoob'
emails[1] = 'tamara@vivo'
emails[2] = 'dolores@leve'
usuarios = {}
tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]
