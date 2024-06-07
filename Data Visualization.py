import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:\\Users\\HP\\Desktop\\Data Visualization\\medium_data.csv.zip'
df = pd.read_csv(file_path)


print(df.head(10))


print(df.shape)


df.drop(['image'], axis=1, inplace=True)

print(df.head(2))

column_titles = ['id', 'date', 'title', 'subtitle', 'publication', 'claps', 'reading_time', 'responses', 'url']
df = df.reindex(columns=column_titles)

print(df.head(2))

df.rename(columns={
    'title': 'TITLE', 'subtitle': 'SUBTITLE', 'id': 'ID', 'claps': 'CLAPS',
    'responses': 'RESPONSES', 'reading_time': 'READING TIME', 'date': 'DATE',
    'publication': 'PUBLICATION', 'url': 'URL'
}, inplace=True)


print(df.columns)


numeric_cols = df.select_dtypes(include=np.number).columns
df['Total'] = df[numeric_cols].sum(axis=1)


print(df.describe())

print(df.isnull().sum())


df.sort_values(by='Total', ascending=False, axis=0, inplace=True)


df_top5 = df.head(5)


df_top5 = df_top5[['CLAPS', 'PUBLICATION']].transpose()
print(df_top5)


print(df['CLAPS'].min())


print(df['CLAPS'].max())


print(df['PUBLICATION'].value_counts())


print(df['PUBLICATION'].value_counts() * 100 / len(df))


df['PUBLICATION'].value_counts().plot(kind='bar', figsize=(14, 8))
plt.title('TYPES OF PUBLICATION')
plt.ylabel('COUNT')
plt.show()


print(df["READING TIME"].mean())


print(df.loc[df['CLAPS'] == df['CLAPS'].max(), 'TITLE'])


print(df.loc[4552, 'TITLE'])


print(df.loc[df['RESPONSES'] == df['RESPONSES'].max(), 'TITLE'])


print(df.loc[3977, 'TITLE'])


print(df.loc[6392, 'TITLE'])


print(df.loc[df['CLAPS'] == df['CLAPS'].max(), 'PUBLICATION'])


print(df.loc[df['RESPONSES'] == df['RESPONSES'].max(), 'PUBLICATION'])

