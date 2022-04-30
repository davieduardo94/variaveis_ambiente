import os
from dotenv import load_dotenv
# carregando variaveis
load_dotenv()


# pegando as variaveis de ambiente do usuario
usuario = os.environ['usuario']
senha = os.environ['senha']
print(f'Variaveis carregadas: {usuario} e {senha}')

