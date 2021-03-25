from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()
contador = 0

for i in eq:
    if contador < 20:
        equipos.append(i.text)
    else:
        break
    contador+=1

#Puntos

pt = soup.find_all('td', class_='destacado')

puntos = list()
contador = 0

for i in pt:
    if contador < 20:
        puntos.append(i.text)
    else:
        break
    contador+=1

df = pd.DataFrame({'Nombre':equipos,'Puntos':puntos}, index=list(range(1,21)))

print(df)