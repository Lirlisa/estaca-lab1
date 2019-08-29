from pandas import read_csv
import pandas as pd

nom_arc = "limpieza.csv"
df = read_csv(nom_arc)
#Se estandariza el texto en la tabla
for columna in df:
    df[columna] = df[columna].str.lower()
    
df["genero"] = df["genero"].replace("masculino", "M")
df["genero"] = df["genero"].replace("hombre", "M")
df["genero"] = df["genero"].replace("femenino", "F")
df["genero"] = df["genero"].replace("mujer", "F")

#Se separa la columna 'trabajo' en 2
aux = df["trabajo"].str.split(r"/")
l1=list()
l2=list()
for x in aux:
    l1.append(x[0])
    l2.append(x[1][1:])

df.drop("trabajo", axis=1, inplace=True)
df.insert(loc=3, column="trabajo", value=l1)
df.insert(loc=4, column="sueldo", value=l2)

print(df.to_string(index=False))