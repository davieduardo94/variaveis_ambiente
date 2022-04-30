# Como usar variaveis de ambiente para guardar senhas e keys de forma segura
### Crie um arquivo .env
O arquivo deve estar salvo dentro da pasta do projeto. Esse arquivo deve conter os dados importantes como usuario e senha

EX:
 usuario = "seu_usuario"
 senha = "sua_senha"

Salve o arquivo sem nome, apena como ".env" de modo que esta seja sua extensão

### No seu projeto
- Instale o modulo dotenv
```py
pip install python-dotenv
```
Crie um arquivo do tipo .py e importe os modulos

```py
import os
from dotenv import load_dotenv
load_dotenv()
...
```
Faça o teste e verifique se as configurações estão corretas
```py
...
usuario = os.environ["usuario"]
senha = os.environ["senha"]
print(f'Variaveis carregadas: {usuario} e {senha}')
```

