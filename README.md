# Mini Projeto - Análise Exploratória de Dados

## Objetivo

# 📊 Desafio de Análise de Dados de E-commerce Premium

Este repositório contém um desafio prático de manipulação de dados e inteligência de negócios utilizando Python e a biblioteca **Pandas**. O objetivo é simular cenários reais do cotidiano de um Analista/Cientista de Dados em uma empresa de comércio eletrônico.

## 📂 Sobre a Base de Dados

O arquivo `avaliacoes_premium.csv` gerado contém **100 registros** de compras com as seguintes colunas:

* `id_pedido`: Identificador único do pedido.
* `cliente`: Nome fictício do comprador.
* `genero`: Gênero cadastrado (M, F, Outro).
* `idade`: Idade do cliente.
* `uf`: Estado da federação onde a compra foi realizada.
* `produto`: Item adquirido.
* `valor_compra`: Valor total do produto em reais.
* `nota_avaliacao`: Nota de 1 a 5 dada ao produto/atendimento.
* `comentario`: Texto descritivo do feedback do cliente.
* `status_suporte`: Situação atual do atendimento pós-venda (`Resolvido`, `Pendente`, `Em Aberto` ou `Não Necessário`).

---

## 🎯 Os Desafios (Nível Hard)

Você deve criar um script ou um notebook no Google Colab para responder às seguintes demandas de negócio:

### 🧮 1. O Prejuízo em Risco (Análise Financeira Crítica)
O time financeiro precisa mapear o impacto financeiro dos clientes que tiveram experiências ruins.
* **Missão:** Filtre todos os clientes insatisfeitos (Nota menor ou igual a 2) que possuem chamados de suporte com o status `Pendente` ou `Em Aberto`. Calcule a soma total do `Valor_Compra` desses clientes para descobrir o montante financeiro que está em risco de sofrer *chargeback* ou cancelamento.

### 🗺️ 2. Perfil de Consumo Regional (Agrupamento Avançado)
A equipe de expansão quer entender a demografia do faturamento.
* **Missão:** Agrupe a base de dados por **UF (Estado)**. Para cada estado, exiba:
    1. O ticket médio (média do valor gasto).
    2. A idade média dos compradores.
    3. O volume total de pedidos realizados.
* *Dica: Ordene o resultado final pelos estados com maior ticket médio.*

### 🏷️ 3. Engenharia de Recursos (Categorização de Sentimento)
Para alimentar um futuro modelo de Machine Learning, precisamos normalizar os textos avaliativos de forma categórica.
* **Missão:** Crie uma função de classificação de sentimento baseada na `Nota_Avaliacao`:
    * Notas 4 e 5 $\rightarrow$ `Positivo`
    * Nota 3 $\rightarrow$ `Neutro`
    * Notas 1 e 2 $\rightarrow$ `Negativo`
* Aplique essa função para criar uma nova coluna chamada `Sentimento` no DataFrame e exiba a contagem exata de quantos pedidos se encaixam em cada categoria (`value_counts`).

---

## 🚀 Como Começar

1. Carregue o arquivo `avaliacoes_premium.csv` no seu ambiente Python:
   ```python
   import pandas as pd
   df = pd.read_csv('avaliacoes_premium.csv')



2. Crie uma branch para voce realizar sua resolução
    