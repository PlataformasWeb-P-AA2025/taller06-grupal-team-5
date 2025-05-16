from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base2 import Country

import requests
import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///tableCountries.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
datos = requests.get(url)
# archivo = request.get("------------------.json")
datos_json =  datos.json() # paso los datos del archivo a json
# archivo.json()
documentos = datos_json


for d in documentos:
    country = Country()
    country.name = d.get("CLDR display name")
    country.capital = d.get("Capital")
    country.continent = d.get("Continent")
    country.dial = d.get("Dial")
    geoname_id = d.get("Geoname ID")
    country.geoname_id = int(geoname_id) if geoname_id is not None else None
    country.itu = d.get("ITU")
    country.languages = d.get("Languages")
    country.is_independent = (str(d.get("is_independent") or "").lower() == "yes")
    session.add(country)
'''
for d in documentos:  
   country = Country()
   country.name = d.get("CLDR display name")
   country.capital  = d.get("Capital")
   country.continent = d.get("Continent")
   country.dial = d.get("Dial")
   country.geoname_id = int(d.get("Geoname ID")) if d.get("Geoname ID") else None 
   country.itu  = d.get("ITU") 
   country.languages = d.get("Languages") 
   country.is_independent = (d.get("is_independent","").lower() == "yes") 
   session.add(country) 
    '''
# confirmar transacciones

session.commit()
