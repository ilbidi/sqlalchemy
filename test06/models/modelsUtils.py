# Utilita' classe models
import unittest
import sqlalchemy

from models import Base, User, SensorType
from . import Session

session = Session()

def insertSensorType(code, description=None):
    """Insert SensorType or update if already existing"""
    sensorType = session.query(SensorType).filter_by(code=code).first()
    if sensorType is None:
        sensorType = SensorType(code=code, description=description )
        session.add(SensorType)
        session.commit()
    else:
        sensorType.description=description
        session.commit()
    session.rollback()
