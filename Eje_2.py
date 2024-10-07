import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
Animal_df = pd.read_csv('Animal Dataset.csv')

conservation_status = Animal_df['Conservation Status'].value_counts()

#Creamos el grafico de barras
conservation_status.plot(kind='bar', color='orange')
plt.title('Cantidad de especies por estado de conservación')
plt.xlabel('Estado de conservación')
plt.ylabel('Cantidad de especies')
plt.xticks(rotation=45)
plt.show()

#GRAFICO DE BARRAS

"""En ese grafico se genera un grafico de tipo de barra en el cual se presenta la cantidad de especies y tambien
su estado de conservacion"""