import pandas as pd

#Cargar la base de datos desde un archivo CSV

data = pd.read_csv('rating.csv')

#Mostrar las primeras filas de la base de datos

print(data.head())