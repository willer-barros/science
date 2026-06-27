import pandas as pd
import numpy as np

# Semente para manter os dados consistentes
np.random.seed(42)

produtos = ['Smartphone', 'Fone Bluetooth', 'Notebook', 'Smartwatch', 'Teclado Mecânico', 
            'Monitor Gamer', 'Mouse Sem Fio', 'Cadeira Ergonômica', 'Caixa de Som', 'Tablet']

comentarios_ruins = [
    'O produto parou de funcionar na primeira semana. Péssimo.',
    'Entrega atrasou muito e a embalagem veio totalmente amassada.',
    'Não gostei da qualidade do material, parece muito frágil.',
    'Trava o tempo todo e o suporte da empresa não me respondeu.',
    'Veio faltando peças na caixa. Estou muito insatisfeito.'
]

comentarios_bons = [
    'Excelente produto, superou todas as minhas expectativas!',
    'Melhor compra que fiz este ano, recomendo muito.',
    'Chegou super rápido e funciona perfeitamente.',
    'Muito robusto e de ótima qualidade. Vale cada centavo.',
    'Design bonito e entrega antes do prazo.'
]

dados = []
for i in range(1, 101):
    nota = int(np.random.choice([1, 2, 3, 4, 5], p=[0.15, 0.10, 0.15, 0.25, 0.35]))
    comentario = np.random.choice(comentarios_bons) if nota >= 4 else (np.random.choice(comentarios_ruins) if nota <= 2 else 'O produto é mediano, atende o básico.')
    
    dados.append({
        'ID_Pedido': f'REQ-{1000 + i}',
        'Cliente': f'Cliente {i}',
        'Genero': np.random.choice(['M', 'F', 'Outro']),
        'Idade': int(np.random.randint(18, 65)),
        'UF': np.random.choice(['SP', 'RJ', 'MG', 'SC', 'PR', 'RS', 'BA', 'PE']),
        'Produto': np.random.choice(produtos),
        'Valor_Compra': round(float(np.random.uniform(50.0, 4500.0)), 2),
        'Nota_Avaliacao': nota,
        'Comentario': comentario,
        'Status_Suporte': np.random.choice(['Resolvido', 'Pendente', 'Em Aberto'], p=[0.6, 0.2, 0.2]) if nota <= 3 else 'Não Necessário'
    })

df_100 = pd.DataFrame(dados)
df_100.to_csv('avaliacoes_premium.csv', index=False)
print("✅ Planilha 'avaliacoes_premium.csv' gerada com sucesso no ambiente!")