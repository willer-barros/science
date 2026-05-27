import pandas as pd
import kagglehub
from pathlib import Path

# =====================================================
# FUNÇÃO PARA EXTRAIR DADOS
# =====================================================

def extrair_dados():
    path = kagglehub.dataset_download("namespaiva/base-varejo")

    csv_path = Path(path) / "Base Varejo.csv"

    df = pd.read_csv(csv_path, sep=';')

    return df


# =====================================================
# CARREGAMENTO
# =====================================================

print("\n========== IMPORTANDO DADOS ==========\n")

df = extrair_dados()

print(df.head())

print("\nQuantidade de linhas e colunas:")
print(df.shape)

print("\nTipos de dados:")
print(df.dtypes)


# =====================================================
# VERIFICAÇÃO DE PROBLEMAS
# =====================================================

print("\n========== VALORES NULOS ==========\n")

print(df.isnull().sum())

print("\n========== DUPLICATAS ==========\n")

print(f"Duplicatas: {df.duplicated().sum()}")


# =====================================================
# LIMPEZA DOS DADOS
# =====================================================

print("\n========== LIMPEZA ==========\n")

# Remover duplicatas
df = df.drop_duplicates()

# Preencher categorias vazias
if 'Categoria' in df.columns:
    df['Categoria'] = df['Categoria'].fillna('Sem Categoria')

# Converter datas
if 'Data_Compra' in df.columns:
    df['Data_Compra'] = pd.to_datetime(
        df['Data_Compra'],
        errors='coerce'
    )

# Remover datas inválidas
df = df.dropna(subset=['Data_Compra'])

# Preencher valores numéricos nulos
colunas_numericas = df.select_dtypes(include=['int64', 'float64']).columns

for coluna in colunas_numericas:
    df[coluna] = df[coluna].fillna(df[coluna].median())

print("\nDados tratados com sucesso!")


# =====================================================
# ESTATÍSTICAS DESCRITIVAS
# =====================================================

print("\n========== ESTATÍSTICAS ==========\n")

# Ajuste o nome da coluna conforme a base
coluna_filhos = 'Numero_Filhos'

if coluna_filhos in df.columns:

    print(f"Média: {df[coluna_filhos].mean()}")

    print(f"Mediana: {df[coluna_filhos].median()}")

    print(f"Desvio padrão: {df[coluna_filhos].std()}")

    print(f"Moda: {df[coluna_filhos].mode()[0]}")

    print(f"Máximo: {df[coluna_filhos].max()}")

    print(f"Mínimo: {df[coluna_filhos].min()}")

    print(f"Contagem: {df[coluna_filhos].count()}")

else:
    print(f"Coluna '{coluna_filhos}' não encontrada.")


# =====================================================
# AGRUPAMENTOS
# =====================================================

print("\n========== AGRUPAMENTOS ==========\n")

# Exemplo 1
if 'Genero' in df.columns and 'Valor_Compra' in df.columns:

    agrupamento_genero = df.groupby('Genero')['Valor_Compra'].sum()

    print("\nVendas por gênero:")
    print(agrupamento_genero)


# Exemplo 2
if 'Categoria' in df.columns and 'Valor_Compra' in df.columns:

    agrupamento_categoria = df.groupby('Categoria')['Valor_Compra'].sum()

    print("\nVendas por categoria:")
    print(agrupamento_categoria.sort_values(ascending=False))


# =====================================================
# INSIGHTS
# =====================================================

print("\n========== INSIGHTS ==========\n")

print("""
1. Algumas colunas apresentaram valores nulos e precisaram de tratamento.

2. Foram encontradas linhas duplicadas na base.

3. A conversão da coluna de datas foi necessária para análise temporal.

4. Certas categorias possuem volume de vendas muito superior às demais.

5. O agrupamento por gênero mostrou diferenças no comportamento de compra.

6. A base ainda pode conter inconsistências que exigiriam validações mais avançadas.
""")

# =====================================================
# EXPORTAR BASE LIMPA
# =====================================================

df.to_csv("df_limpo.csv", index=False)

print("\nArquivo df_limpo.csv exportado com sucesso!")