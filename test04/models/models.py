# Modelli per gestione tabelle
import sqlalchemy
import json

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Classe User per gestione utenti
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

# Classe device type
#     tipo di dispositivo che esegue la comunicazione, ad esempio
#     arduino
class DeviceType(Base):
    # Table name
    __tablename__ = 'device_type'
    # Fields
    id = Column(Integer, primary_key = True)
    code = Column(String(100))
    description = Column(String(100))

    # Show content
    def __repr__(self):
        return '<DeviceType(''code''=%s, ''description''=%s)>' % \
            (self.code, self.description)
    
    # Check equals
    def __eq__(self, other):
        return isinstance(other, DeviceType) and other.id == self.id

# Classe sensor type
#     Tipo di sensore che trasmette i dati
#     ad esempio HumiditySensor
class SensorType(Base):
    # Table name
    __tablename__ = 'sensor_type'
    # Fields
    id = Column(Integer, primary_key = True)
    code = Column(String(100))
    description = Column(String(100))

    # Show content
    def __repr__(self):
        return '<SensorType(''code''=%s, ''description''=%s)>' % \
            (self.code, self.description)
    
    # Check equals
    def __eq__(self, other):
        return isinstance(other, SensorType) and other.id == self.id

    
# Classe device
#     Nome univoco di un dispositivo
class Device(Base):
    # Table name
    __tablename__ = 'device'
    # Fields
    id = Column(Integer, primary_key = True)
    code = Column(String(100))
    description = Column(String(100))
    # TODO Device type
    # TODO list of sensors

    # Show content
    def __repr__(self):
        return '<Device(''code''=%s, ''description''=%s)>' % \
            (self.code, self.description)
    
    # Check equals
    def __eq__(self, other):
        return isinstance(other, Device) and other.id == self.id

# Classe data
#    Dati ricevuti dai sensori dei dispositivi
class DeviceData(Base):
    # Table name
    __tablename__ = 'device_data'
    # Fields
    id = Column(Integer, primary_key = True)
    # TODO timestamp
    # TODO device
    value = Column(Float)
    # Show content
    def __repr__(self):
        return '<DeviceData(''value''=%f>' % \
            (self.value)
    
    # Check equals
    def __eq__(self, other):
        return isinstance(other, DeviceData) and other.id == self.id
    
