import pandas as pd
import matplotlib.pyplot as plt

# Aqui se carga el dataset de jugadores de fútbol
football_df = pd.read_csv('players.csv')

# Crear el gráfico de líneas
plt.plot(football_df['Name'], football_df['Club'], 'o', color='green', markersize=2)
plt.title('Relación entre Nombre y su club')
plt.xlabel('Nombre')
plt.ylabel('Nombre de su club')
plt.grid(True)
plt.show()

#GRAFICO DE LINEAS
#https://www.kaggle.com/code/desalegngeb/english-premier-league-players-statistics

""" En este grafico se puede apreciar que se genera un grafico de lines en el cual presenta el nombre del jugador
y tambien presenta en que equipo el juegador juega actualmente"""

