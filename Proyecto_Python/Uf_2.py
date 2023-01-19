import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sqlite3

def actualizar_uf():
    url = "https://si3.bcentral.cl/Indicadores/secure/Indicadores.aspx"        # Realizar petición a la página web
    reqs = requests.get(url)                                                    # Llamar url co método get
    soup = BeautifulSoup(reqs.text, 'html.parser')                              # Utilizar BeautifulSoup para extraer la información
    uf = soup.find('span', {'id': 'lblValor1'}).text                            # Buscar el valor de la UF en la página
    print("Valor actual de la UF:", uf)
    df = pd.DataFrame({"UF": [uf]})                                             # Crear un DataFrame con la información
    df.to_csv('')                                                  #guardar en un archivo o base de datos
    print("Valor de la UF para utilizar:", df.loc[0, "UF"])                     # Utilizar el valor actualizado de la UF

while True:
    actualizar_uf()
    time.sleep(86400)     #Actualizar cada día


    #"uf_values.csv"

# Crear conexión a la base de datos
#conn = sqlite3.connect("uf_values.db")
#cursor = conn.cursor()


# Crear tabla para almacenar el valor de la UF

#cursor.execute(                                    
#    CREATE TABLE uf_values (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        value FLOAT,
#        date DATE
#    )
#    )
#conn.commit()

# Insertar el valor de la UF en la tabla
#cursor.execute(
#    INSERT INTO uf_values (value, date)
#    VAL
#     )