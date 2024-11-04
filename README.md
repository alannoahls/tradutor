
=======
# Tradutor 

Este projeto é um tradutor simples em Python que extrai texto de URL e traduz para o idioma desejado.

## Funcionalidade

- O programa extrai o texto do primeiro parágrafo da página da URL (questão de desempenho deixei o primeiro parágrafo)
- O texto é traduzido usando a biblioteca `googletrans`.
- O resultado é salvo em um arquivo de texto.

## Resumo

- **`.env`**: Armazena as chaves de API. (quando for integrar com os serviços Azure)
- **`config.py`**: Carrega as variáveis do `.env`.
- **`tradutor.py`**: Lógica de tradução.
- **`main.py`**: Executa o programa.
- **`requisitos.txt`**: Lista as bibliotecas necessárias.

Assim você poderá gerenciar cada parte do projeto em arquivos separados que eu fiz no PyCharm, que ajuda na organização e na futura migração ao Azure.

## Como usar

1. Execute o script `main.py`.
2. O texto da página da Wikipedia será extraído e traduzido.
3. O resultado será salvo em `documento_traduzido.txt`.

## Futuro

- Planejo expandir este projeto para integrar com serviços do Azure, pois não consegui ter acesso ao portal Azure onde era pra ter sido feito o projeto mais robusto e com acesso ao OpenAI chatgpt
- fiz esse para demonstrar que entendi o conteúdo da aula do bootcamp DIO
>>>>>>> b23b7b68c0165e3b060fbd21fb6e9db19871f7ce
