# Classificação de Comentários de Notícias com BERT

Este repositório se trata do Trabalho 2 de Inteligência Artificial que aplica o modelo **BERT** para classificar comentários de notícias em **sentimentos** (negativo, neutro e positivo), utilizando o token **[CLS]** como representação do texto.

A base usada é a planilha de comentários sobre a reportagem das onças, contendo a coluna `comment_text` e colunas de rótulos como `onca`, `caseiro`, `fake news`, `ironia` e `notícia`.
Foram escolhidas 3 classes (`onça`, `caseiro`, `notícia`) e cada uma dessas classes possui rótulos textuais próprios, que foram convertidos para valores numéricos conforme o enunciado (0, 1 e 2).
---

## Arquivos

Treinar um modelo BERT para:

- Ler comentários de notícias/vídeos (`comment_text`);
- Classificar o sentimento em **negativo**, **neutro** ou **positivo**;
- Utilizar o vetor do token **[CLS]** como representação do texto;
- Avaliar o modelo com **accuracy, precision, recall e F1-score** e mostrar gráficos de Loss e Accuracy;
- Mostrar exemplos de textos que o modelo classificou errado.

---

- `utils.py`  
  Funções auxiliares usadas no notebook. Exemplo:

```text
data/
 ├─ oncas_comentarios.csv   # base de dados com os comentários e rótulos
 └─ README.md               # descrição rápida da base

notebooks/
 └─ 01_treinamento_bert.ipynb   # notebook principal com todo o experimento

src/
 ├─ __init__.py             # marca o diretório como pacote Python
 └─ utils.py                # funções auxiliares 

README.md                   #readme resumo do projeto

requirements.txt            # dependências do projeto (torch, transformers, etc.)

## Como usar 

1. Crie um ambiente virtual python -m venv
2. Instale as dependências com `pip install -r requirements.txt`.
3. Abra o notebook `notebooks/01_treinamento_bert.ipynb` (no VSCode ou no Google Colab).
4. Siga as seções do notebook para carregar os dados, treinar e avaliar o modelo.
```

## Executar no Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/victorssanches/bert-classificacao-noticias/blob/main/notebooks/01_treinamento_bert%20(1).ipynb)

## Resultados
- **Acurácia de validação** ficou entre **0.78 e 0.82**
- **Acurácia de teste** variou entre **0.80 e 0.83**
- Leve **overfitting**, esperado pelo desequilíbrio das classes
- Classes neutras tiveram melhor desempenho  
- Classes minoritárias (positivo/ruim) mostraram menor F1-score
> *Observação: cada tarefa foi treinada com um BERT novo, usando o mesmo pipeline genérico.*


