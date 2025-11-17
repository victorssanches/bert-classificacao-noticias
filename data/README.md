# Pasta `data/`

Esta pasta armazena os arquivos de dados usados no projeto

## Arquivos

- `oncas_comentarios.csv`  
  Arquivo CSV com os comentários e os rótulos usados no trabalho.

  Principais colunas:
  - `comment_text`: texto do comentário.
  - `onca`, `caseiro`, `fake news`, `ironia`, `notícia`:  
    cada uma dessas colunas traz um rótulo de **sentimento** em relação ao comentário com valores, por exemplo:
    - `negativo`
    - `neutro`
    - `positivo`

No notebook principal (`notebooks/01_treinamento_bert.ipynb`), uma dessas colunas é
selecionada como alvo (`label`) por vez, e o modelo BERT é treinado para prever
`negativo`, `neutro` ou `positivo` para aquela coluna.
