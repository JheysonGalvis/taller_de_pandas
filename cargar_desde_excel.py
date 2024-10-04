import pandas as pd

# Leer archivo Excel
data = pd.read_excel('animeflv.xlsx')

# Mostrar las primeras filas de la base de datos
print(data.head())
