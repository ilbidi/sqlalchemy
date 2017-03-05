# Modelli per gestione tabelle
import sqlalchemy
import json

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # Table name
    __tablename__ = 'user'
    # Fields
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    fullname = Column(String(100))
    password = Column(String(100))

    # Show content
    def __repr__(self):
        return '<User(''name''=%s, ''fullname''=%s, ''password''=%s)>' % (self.name, self.fullname, self.password)
    

    # Check equals
    def __eq__(self, other):
        return isinstance(other, User) and other.id == self.id
