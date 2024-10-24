import pandas as pd

pd.read_excel('/Users/eliaskehrli/Library/Mobile Documents/com~apple~CloudDocs/Uni/Master/Sport/SSR Basismodul/programming_basics/Final_Project/testdata.xlsx')

df = pd.read_excel('/Users/eliaskehrli/Library/Mobile Documents/com~apple~CloudDocs/Uni/Master/Sport/SSR Basismodul/programming_basics/Final_Project/testdata.xlsx')

df.columns = df.iloc[390]
df.iloc[391:395]

