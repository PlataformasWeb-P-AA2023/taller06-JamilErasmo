from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///Genera_base.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Persona(Base):
    __tablename__ = 'laspersonas'
    
    id = Column(Integer, primary_key=True)

    Nombredepais = Column(String)
    Capital = Column(String)
    Continente = Column (String)
    Dial = Column(String)
    GeonameID = Column(String)
    ITU = Column(String)
    Lenguajes = Column(String)
    Siesindependiente = Column(String)



Base.metadata.create_all(engine)
