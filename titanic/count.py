import pandas as pd

df = pd.read_csv('./train.csv', encoding='UTF-8')

print(df['Embarked'].value_counts())
