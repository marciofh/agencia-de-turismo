import pandas as pd
import re
df = pd.read_excel('./EXTRATO_TOTAL.xlsx')

df['preco'] = df['preco'].map(lambda x: re.sub('[^0-9-,]', '', x))
df['preco'] = df['preco'].map(lambda x: re.sub(',', '.', x))

print(df)