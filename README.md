# Pokédex Desktop

Aplicativo desktop desenvolvido em Python para consultar informações sobre Pokémon usando a [PokéAPI](https://pokeapi.co/).

## Funcionalidades

- Busca de Pokémon por nome, com autocompletar
- Exibição de imagens oficiais nas versões normal e shiny
- Consulta de altura, peso, tipos e habilidades
- Adição e remoção de Pokémon favoritos, com armazenamento local
- Lista de favoritos na tela principal
- Alternância entre tema claro e escuro
- Cache local dos Pokémon já consultados
- Tratamento de erros de busca e conexão
- Interface gráfica construída com Tkinter

## Tecnologias

- Python 3.x
- Tkinter
- Requests
- Pillow (PIL)
- JSON para dados locais e cache
- PokéAPI

## Como executar

É necessário ter Python 3.x instalado. No terminal, clone o repositório e instale as dependências:

```bash
git clone https://github.com/LucasBarros0/UC5-main.git
cd UC5-main
python -m pip install requests pillow
```

Depois, inicie a aplicação:

```bash
python app.py
```

A conexão com a internet é necessária para consultar a PokéAPI. O cache permite acessar informações de Pokémon que já foram carregadas anteriormente.

## Estrutura principal

- `app.py`
- `models.py`
- `services/`
- `ui/`
- `favorites.json` — dados dos favoritos
- `poke_cache.json` — cache local

## Créditos

Os dados são fornecidos pela [PokéAPI](https://pokeapi.co/).
