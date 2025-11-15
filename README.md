# Classificação de Comentários de Notícias com BERT

Este projeto é o esqueleto para o Trabalho 2 de Inteligência Artificial.

## Objetivo

Treinar um modelo BERT para classificar comentários de notícias em três classes (por exemplo: onça, fake news, ironia),
utilizando o token `[CLS]` como representação do texto.

## Estrutura de pastas

```text
.
├─ data/
│  └─ (coloque aqui o arquivo CSV com os comentários)
├─ notebooks/
│  └─ 01_treinamento_bert.ipynb
├─ src/
│  ├─ __init__.py
│  └─ utils.py
└─ requirements.txt
```

## Como usar (resumo)

1. Crie um ambiente virtual (opcional, mas recomendado).
2. Instale as dependências com `pip install -r requirements.txt`.
3. Abra o notebook `notebooks/01_treinamento_bert.ipynb` (no VSCode ou no Google Colab).
4. Siga as seções do notebook para carregar os dados, treinar e avaliar o modelo.