import pandas as pd

# URL = "https://docs.google.com/spreadsheets/d/1SJwACgit1fHDUMnIITbhDponhl-CK5RipWNV_jTN3lc/export?format=csv"

URL = "planilhas/dados_clientes.csv"


df = pd.read_csv(URL)
print(df)

# verificar clientes insatisfeitos
clientes_insatisfeitos = df[df["Nota_Avaliacao"] <= 2]
print("Clientes Insatisfeitos que precisam de atenção: ")
print(clientes_insatisfeitos)