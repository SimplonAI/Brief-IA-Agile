from __future__ import annotations
from sqlalchemy.engine import create_engine
import json

from .models import Base

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




Base.metadata.create_all(connection)





