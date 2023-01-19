from bs4 import BeautifulSoup
import requests

url = 'https://www.bcentral.cl/inicio'                                           #url de bcentral
html = requests.get(url).content                                                 #Llamar url con método GET

soup = BeautifulSoup(html, 'html.parser')                                        #Extraer datos HTML
valor_uf = soup.find('div', {'class': 'valor-uf'}).text                          #Traer la class desde código HTML
print(valor_uf)