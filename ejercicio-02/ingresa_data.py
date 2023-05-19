from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests

from crear_base import Country

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///Country.db')


Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

documento = archivo.json()


for d in documento:
    print(d)
    print(len(d.keys()))
    p = Country(nombre_Pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoname_Id=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], \
                independiente=d['is_independent'])
    session.add(p)

session.commit()