import pandas as pd

# URL = "https://docs.google.com/spreadsheets/d/1SJwACgit1fHDUMnIITbhDponhl-CK5RipWNV_jTN3lc/export?format=csv"

URL = "planilhas/dados_clientes.csv"


df = pd.read_csv(URL)
print(df)

# verificar clientes insatisfeitos
clientes_insatisfeitos = df[df["Nota_Avaliacao"] <= 2]
print("Clientes Insatisfeitos que precisam de atenção: ")
print(clientes_insatisfeitos)

#material para extrair KPI's

nota_media = df['Nota_Avaliacao'].mean()
print(f"📊 A nota média da nossa empresa é: {nota_media:.2f} de 5.0")

# 1. Filtrando os promotores da marca (Nota igual a 5)
clientes_vips = df[df['Nota_Avaliacao'] == 5]

print("🎉 Clientes Ouro identificados para campanha de Marketing:")
clientes_vips[['Cliente', 'Produto']]