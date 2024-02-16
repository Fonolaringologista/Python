import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACa384b6364e4d57b458d269030ee4138d"
auth_token  = "1626e1617096a2820ed47981b4ebd27b"

client = Client(account_sid, auth_token)


#passo a passo

#abrir os 6 arquivos xls
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
            #pandas retorna no formato de tabelas. values[0] faz com que retorne como texto
        print(f'No mês {mes} encontrou alguem com mais de 55k; Vendedor: {vendedor}, Vendas: {vendas}')
        #as chaves indicam variaveis
        message = client.messages.create(
            to="+5561995952862",
            from_="++13416675669",
            body=f'No mês {mes} encontrou alguem com mais de 55k; Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)



#tabela_vendas_janeiro = pd.read_excel('janeiro.xlsx')
#tabela_vendas_fevereiro = pd.read_excel('fevereiro.xlsx')
#tabela_vendas_março = pd.read_excel('março.xlsx')
#tabela_vendas_abril = pd.read_excel('abril.xlsx')
#tabela_vendas_maio = pd.read_excel('maio.xlsx')
#tabela_vendas_junho = pd.read_excel('junho.xlsx')

#para cada arquivo:
    #verificar se algum mes maior do que 55k

    #se for maior -> enviar SMS com nome, mês e vendas
        #usar Twilio para enviar o SMS
    #se for menor -> nao fazer nada

#instalar bibliotecas
    #pandas
    #openpyxl
    #Twilio
    #pyarrow