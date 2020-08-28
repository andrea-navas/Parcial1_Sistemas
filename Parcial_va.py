import pandas as pd 
df = pd.read_csv('winequality-red.csv', sep=';')

def evaluacion(compuestos_media, compuestos):
    for A, PH in enumerate(compuestos):
        if PH >= compuestos_media:
            df.loc[A, PH] = 'alto'
        else:
            df.loc[A, PH] = 'bajo'
    ph_compuestos = df.groupby(PH).quality.mean()
    return print(ph_compuestos) 

#Media de los compuestos del vino rojo. 
mediaph_alcohol = df.alcohol.median()
mediaph_citric_acid = df.citric_acid.median()
mediaph_residual_sugar = df.residual_sugar.median()
mediaph_PH = df.pH.median()

#compuestos
alcohol = evaluacion(mediaph_alcohol, df.alcohol)
citric_acid = evaluacion(mediaph_citric_acid, df.citric_acid)
residual_sugar = evaluacion(mediaph_residual_sugar, df.residual_sugar)
pH = evaluacion(mediaph_PH, df.pH) 