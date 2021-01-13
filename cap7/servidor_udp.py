from socket import *

servidor = '127.0.0.1'
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))
print('Servidor pronto...')

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print(f'Origem... {origem}')
    print(f'Dados recebidos: {dados.decode()}')
    resp = input('Digite a resposta: ')
    obj_socket.sendto(resp.encode(), origem)

obj_socket.close()
