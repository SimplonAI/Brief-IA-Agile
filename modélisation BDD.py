from __future__ import annotations
from re import I
from sqlalchemy import Column, Integer, VARCHAR, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, Enum
import json


## IMPORT DU CONFIG.JSON
# assignation de la config.json à fichierConfig
fichierConfig = "config.json"
# ouverture et chargement des donnée contenu dans fichierConfig
with open(fichierConfig) as fichier:
    config = json.load(fichier)["Postgres"]

class SqlORM():
    def __init__(self,config):
        self.config = config
        self.connector = self._connect_db()
    def _connect_db(self):
        connector = create_engine(config["connector"] + '://' + config["user"] + ":" + config["password"] + "@" + config["host"] + ":" + config["port"] + "/" + config["bdd"], echo=False)
        return connector

testclass = SqlORM(config)
print(10 * "*")
print("test de la connection", '\n')
connection = testclass.connector
print(connection , '\n')



Base = declarative_base()

class House(Base):
    __tablename__ = 'house'
    id = Column('ho_id', Integer, primary_key=True)
    longitude = Column('ho_longitude', DECIMAL(5,2))
    latitude = Column('ho_latitude', DECIMAL(5,2))
    housing_median_age = Column("ho_housing_median_age", Integer)
    total_rooms = Column("ho_total_rooms",Integer)
    total_bedrooms = Column("ho_total_bedrooms", Integer)
    population = Column("ho_population", Integer)
    households = Column("ho_households", Integer)
    median_income = Column("ho_median_income",DECIMAL(6,4))
    median_house_value = Column("ho_median_house_value", Integer)
    ocean_proximity = Column("ho_ocean_proximity", VARCHAR(10))
    created_date = Column("ho_created_date",DateTime)


class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id = Column('ut_id', Integer, primary_key=True)
    mail = Column('ut_mail', VARCHAR(60))
    password = Column("ut_password", VARCHAR(128))


Base.metadata.create_all(connection)





