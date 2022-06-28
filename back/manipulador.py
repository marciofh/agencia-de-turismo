import pandas as pd

df = pd.read_excel('./back/base.xlsx')



df = df.rename(columns = {0 : 'valores'})
df = df.drop(columns = ['Unnamed: 0'])
passagens = pd.DataFrame()

tamanho = int(len(df) / 5)

for i in range(tamanho):
    voo = df.iloc[:5]
    passagens['coluna ' + str(i)] = voo
    df = df.drop(df.index[:5])
    df.reset_index(inplace = True, drop = True)

passagens = passagens.transpose()
passagens.reset_index(inplace = True, drop = True)
passagens = passagens.rename(columns={0 : 'origem'})
passagens = passagens.rename(columns={1 : 'destino'})
passagens = passagens.rename(columns={2 : 'tempo'})
passagens = passagens.rename(columns={3 : 'conexao'})
passagens = passagens.rename(columns={4 : 'preco'})
passagens['tempo'] = passagens['tempo'].replace(' ,', '', regex = True)



    


