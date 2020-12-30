import pandas as pd

df =pd.read_excel('announce_hindi.xlsx')
print(df)

for index,items in df.iterrows():
    print(items['from'])
    print(items['train_name'])
    print(items['to'])
    print(items['train_no'])
    print(items['via'])
    print(items['platform'])