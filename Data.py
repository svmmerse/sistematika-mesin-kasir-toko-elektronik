import sqlite3
from abc import ABC
#abc = abstract base class

class Data(ABC):

    def __init__(self):
        self.connection = sqlite3.connect('project.db')

    def execute(self,query):
        return self.connection.execute(query)

    def commit(self):
        return self.connection.commit()
        
