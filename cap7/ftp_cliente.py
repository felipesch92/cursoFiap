from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usr = input('Usuário: ')
senha = input('Senha: ')

ftp.login(usr, senha)

print(f'Diretório atual de trabalho: {ftp.pwd()}')

ftp.cwd('pub')

print(f'Diretório corrente: {ftp.pwd()}')

print(ftp.retrlines('LIST'))

ftp.quit()
