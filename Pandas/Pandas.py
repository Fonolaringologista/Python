import pandas as pd

# dataframe = pd.DataFrame()

vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df)
print(vendas_df.head(10))
print(vendas_df.shape)
print(vendas_df.describe())

#Visualização de dados uteis
    #head
    #shape
    #describe

produtos = vendas_df[['Produto', 'ID Loja']]
print(produtos)
#pra localizar uma coluna na tabela, localizar o primeiro item da coluna
    #linhas utilizam de índices para serem localizadas

#.loc - método para localizar linhas, colunas, células
    #pegar linhas que cumprem uma determinada condição
    #padrão .loc[linha, coluna]

print(vendas_df.loc[1])
vendas_norteshp_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['Produto', 'Quantidade']]
print(vendas_norteshp_df)

#Como adicionar uma coluna

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df['Comissão'])

#Como adicionar uma linha

vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
vendas_df = vendas_df._append(vendas_dez_df)
#vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
#print(vendas_df['Comissão'])
#print(vendas_df)

#Excluir linhas ou colunas

#vendas_df = vendas_df.drop('Comissão', axis=1)
    #eixo 0 define linha, eixo 1 define coluna

#Deletar linhas e colunas completamente vazias
vendas_df = vendas_df.dropna(how='all', axis=1)
vendas_df = vendas_df.dropna(how='all', axis=0)

#Linhas que possuam pelo menos um valor vazio
vendas_df = vendas_df.dropna()

#Preencher valores vazios com a média da coluna
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
print(vendas_df)

#Preencher com o primeiro valor imediatamente acima
vendas_df = vendas_df.ffill()

#Fazer a contagem de vezes em que um valor aparece na tabela
trasacoes_loja = vendas_df['ID Loja'].value_counts()
print(trasacoes_loja)

#Fazer agrupamento de uma coluna
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()
print(faturamento_produto)

#Mesclar 2 dataframes
gerentes_df = pd.read_excel('Gerentes.xlsx')
vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)