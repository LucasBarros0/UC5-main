# 📘 Pokédex Desktop App

Uma aplicação desktop feita em Python que consome a PokéAPI para buscar e exibir informações completas sobre Pokémon de forma simples, visual e moderna.

---

## 🔍 Funcionalidades

- 🔎 Buscar Pokémon por nome com autocompletar
- 🖼️ Exibir imagem oficial do Pokémon (normal e shiny)
- 📏 Mostrar altura e peso (em metros e quilos)
- 🧬 Listar tipos e habilidades
- 💖 Adicionar e remover Pokémon dos favoritos (armazenamento local)
- ⭐ Lista de favoritos na tela principal
- 🌙 Alternar entre tema claro e escuro
- ⚡ Cache offline dos Pokémon já buscados
- ⚠️ Tratamento de erros de busca e conexões
- 🖥️ Interface gráfica moderna e intuitiva com Tkinter

---

## 🧰 Tecnologias utilizadas

- **Python 3.x**
- **Tkinter** – interface gráfica
- **Requests** – consumo de APIs
- **Pillow (PIL)** – exibição de imagens
- **JSON** – manipulação e cache de dados
- **PokéAPI** – fonte dos dados dos Pokémon

---

## ▶️ Como rodar o projeto

1. Clone o repositório e acesse a pasta do projeto:

    ```bash
    git clone https://github.com/seu-usuario/pokedex-desktop.git
    cd pokedex-desktop
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    > Se não houver um arquivo `requirements.txt`, instale manualmente:
    > 
    > ```bash
    > pip install requests pillow
    > ```

3. Execute o aplicativo:

    ```bash
    python main.py
    ```

---

## 📸 Screenshots

> Adicione aqui prints da interface principal, detalhes do Pokémon e lista de favoritos.

---

## 📂 Estrutura de Pastas

```
UC5-main/
│
├── services/
│   ├── api_client.py
│   └── favorites.py
│
├── ui/
│   ├── main_window.py
│   └── details_view.py
│
├── poke_cache.json
├── favorites.json
├── main.py
└── README.md
```

---

## 🙋‍♂️ Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto é livre para fins educacionais.

---

## 🤝 Créditos

- [PokéAPI](https://pokeapi.co/) – Fonte dos dados dos Pokémon
- Ícones e sprites oficiais: [PokeAPI Sprites](https://github.com/PokeAPI/sprites)