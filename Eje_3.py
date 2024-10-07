import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de ventas de videojuegos
games_df = pd.read_csv('vgsales.csv')

# aqui se Agrupa por plataforma y se suman las ventas globales
platform_sales = games_df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(5)  # Las 5 plataformas con más ventas

# Crear el gráfico circular
platform_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Proporción de ventas globales por plataforma')
plt.ylabel('')
plt.show()

#https://www.kaggle.com/code/upadorprofzs/eda-video-game-sales/input
"""Y por ultimo en este ejercicio se genera un grafico circular en el cual presenta la consola del videojuego
y la porcion de venta en general de cuanto se ha vendido de cada juego"""