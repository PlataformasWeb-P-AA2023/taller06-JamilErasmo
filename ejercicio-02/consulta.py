from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Country

from ingresa_data import engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la tabla docentes que tengan como valor en
# el atributo especifico
paises = session.query(Country).filter(Country.continente=="NA").all()
paises2 = session.query(Country).filter(Country.continente=="AS").order_by(Country.dial).all()
paises3 = session.query(Country).filter(Country.lenguajes!=None).all()
paises4 = session.query(Country).filter(Country.continente=="EU").order_by(Country.capital).all()
paises5 = session.query(Country).filter(and_(Country.nombre_Pais.like("%uador%"), Country.capital.like("%ito%"))).order_by(Country.nombre_Pais).all()