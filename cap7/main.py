import socket
r = 'S'
while r == 'S':
    url = input('URL: ')
    ip = socket.gethostbyname(url)
    print(f'O IP da URl informada é: {ip}')
    r = input('Continuar? ').upper()
