#import platform
import getpass

'''print(f'Nome da máquina: {platform.node()}')
print(f'Arquitetura: {platform.architecture()}')
print(f'Sistema Operacional: {platform.system()}')
print(f'Versão do SO: {platform.release()}')
print(f'Processador: {platform.processor()}')
print(f'Versão do Python: {platform.python_version()}')'''

print(getpass.getuser())
print(getpass.getpass(input('Digite sua senha: ')))
