import pandas as pd

def codidifcar_genero(gen):
    # Codificacion para la columna "genero"
    if gen in {'hombre', 'masculino'}:
        return 'm'
    return 'f'

# Se crea el Dataframe
df = pd.read_csv("limpieza.csv")

# Se separa la columna "trabajo" en "estado_trabajo" y "salario". Luego se elimina "trabajo".
df[['estado_trabajo', 'salario']] = df.trabajo.str.split('/', expand=True)
df['salario'] = df.salario.apply(lambda sal: sal.replace('$', '')).astype(int)
df = df.drop("trabajo", axis=1)

# Se dejan las columnas "genero" y "mascota" en minusculas y se hace una codificacion para la columna "genero".
df['genero'] = df.genero.apply(lambda gen: gen.lower())
df['mascota'] = df.mascota.apply(lambda mas: mas.lower())
df['genero'] = df.genero.apply(codidifcar_genero)

print(df)