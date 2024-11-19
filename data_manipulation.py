import pandas as pd

data = {
    'rocket':['Falcon 1','Falcon 9','Falcon Heavy'],
    'launches':[5,100,3]
}

df = pd.DataFrame(data)
print(df)

print('>>>>')
print(df['rocket'])

print('>>>>')
falcon9_df = df[df['rocket'] == 'Falcon 9']
print(falcon9_df)

print('>>>>')
df['success_rate'] = [0.4,0.98,1.0]
print(df)