from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite


#Integrantes: Richard Ortiz, Agusto Davila
engine = create_engine('sqlite:///tableCountries.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean

class Country(Base):
    __tablename__ = 'countries'
    
    id             = Column(Integer, primary_key=True)
    name           = Column(String)   
    capital        = Column(String)                    
    continent      = Column(String)                
    dial           = Column(String)                    
    geoname_id     = Column(Integer)                   
    itu            = Column(String)                    
    languages      = Column(String)                    
    is_independent = Column(Boolean)                   


Base.metadata.create_all(engine)

