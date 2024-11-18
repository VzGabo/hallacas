import pandas as pd 
import matplotlib.pyplot as plt


class Data: 

    def read_data(self) -> list:
        try: 
            file_path = '../informacion/informacion_calidad_vida.csv'
            dataframe = pd.read_csv(file_path)
        except: 
            print("La data no se encontró")
    
        return dataframe

dataframe = Data().read_data()

# Filtrando los datos de salud
healthy_country_suiza = dataframe[['País', 'Salud', 'Año']]

# Comparando los países por salud
plt.title('Comparación de la salud entre los países en el 2023')
plt.bar(healthy_country_suiza.País, healthy_country_suiza.Salud)
plt.yticks(rotation = 50, color = 'blue', size = 15)
plt.xticks(rotation = 50, size = 12)
plt.show()

country_suiza = dataframe[dataframe['País'] == 'Siria']
country_noruega = dataframe[dataframe['País'] == 'Noruega']

plt.title('Comparación de la economía entre los países en el 2023')
# PAÍSES GRAFICADOS
plt.plot(country_suiza['Año'], country_suiza['Salud'], color = 'g', label = 'Siria', marker = 'o', linestyle = '-')
plt.plot(country_noruega['Año'], country_noruega['Salud'], color = 'black', label = 'Noruega', marker = 'p', linestyle = '-')

# CONFIGURACIÓN
plt.yticks(rotation = 50, color = 'green', size = 15)
plt.xticks(rotation = 50, size = 12)
plt.legend()
plt.grid(True)
plt.show()


# Filtrando los datos de economía
economy_country_suiza = dataframe[['País', 'Economía y Empleo', 'Año']]

# Comparando los países por economía

plt.title('Comparación de la economía entre los países en el 2023')
plt.bar(economy_country_suiza['País'], economy_country_suiza['Economía y Empleo'], color = 'green')
plt.yticks(rotation = 50, color = 'green', size = 15)
plt.xlabel("Años transcurridos")
plt.ylabel("Transcurso del dinero")
plt.xticks(rotation = 50, size = 12)
plt.show()

# En el tiempo cómo se ha visto dichos paises 

country_suiza = dataframe[dataframe['País'] == 'Siria']
country_noruega = dataframe[dataframe['País'] == 'Noruega']


plt.title('Comparación de la economía entre los países en el 2023')
# PAÍSES GRAFICADOS
plt.plot(country_suiza['Año'], country_suiza['Economía y Empleo'], color = 'g', label = 'Siria', marker = 'o', linestyle = '-')
plt.plot(country_noruega['Año'], country_noruega['Economía y Empleo'], color = 'black', label = 'Noruega', marker = 'p', linestyle = '-')

# CONFIGURACIÓN
plt.yticks(rotation = 50, color = 'green', size = 15)
plt.xticks(rotation = 50, size = 12)
plt.legend()
plt.grid(True)
plt.show()