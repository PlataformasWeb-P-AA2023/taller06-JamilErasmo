from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///Country.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Country(Base):
    __tablename__ = 'Country'
    
    id = Column(Integer, primary_key=True)
    nombre_Pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_Id = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def _repr_(self):
        return "País: geoname_id=%s name=%s capital:%s continent=%s dial:%s itu:%s languages:%s is_independent:%s" % (
                          self.geoname_Id,
                          self.nombre_Pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.itu,
                          self.lenguajes,
                          self.independiente)


Base.metadata.create_all(engine)

