import pandas as pd
import re
df = pd.read_excel('./EXTRATO_TOTAL.xlsx')

df['preco'] = df['preco'].map(lambda x: x[3:10])
df['preco'] = df['preco'].map(lambda x: re.sub('[^0-9,]', '', x))

print(df)