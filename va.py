
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

ma = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= ma:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

mpH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= mpH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

ma = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= ma:
        df.loc[i, 'residual sugar'] = 'alto'
    else:
        df.loc[i, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()

mca = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= mca:
        df.loc[i, 'citric acid'] = 'alto'
    else:
        df.loc[i, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()