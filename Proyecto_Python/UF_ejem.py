from bs4 import BeautifulSoup
import requests

#instalar bs4 con pip install beautifulsoup4

url = 'https://www.bcentral.cl/inicio'                                           #url de bcentral
html = requests.get(url).content                                                 #Llamar url con método GET

soup = BeautifulSoup(html, 'html.parser')                                        #Extraer datos HTML

#acá en la class se entrega la clase que alberga la uf que es:
# basic-text fs-2 f-opensans-bold text-center c-blue-nb-2
valor_uf = soup.find('p', {'class': 'basic-text fs-2 f-opensans-bold text-center c-blue-nb-2'}).text                       #Traer la class desde código HTML
print(valor_uf)
