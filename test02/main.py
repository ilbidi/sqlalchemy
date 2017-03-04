# Test02
# Creazione di tabella e sua modifica in memoria

import sys
import logging
import sqlalchemy
import database
import models

from sqlalchemy.orm import sessionmaker
from database import Base,engine
from models import User

# DB configure

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Display SqlAlchemy version
logging.debug('SqlAlchemy version : %s.'%sqlalchemy.__version__)


def main():
    # Start program
    logging.info('Test02 start')

    logging.debug('Create metadata')
    Base.metadata.create_all(engine)
    logging.debug('Create user Fabio')
    userFabio = User(name='Fabio', fullname='Fabio Bidinotto', password ='pwd')

    # Create a session and persist an object
    logging.debug('Create session')
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(userFabio)
    logging.debug('Added user %s'%userFabio)
    userFabio2 = User(name='Fabio2', fullname='Fabio Bidinotto2', password ='pwd')
    session.add(userFabio2)
    logging.debug('Added user %s'%userFabio2)


    # Query tables
    user = session.query(User).filter_by(name='Fabio').first()
    logging.debug('Retieved user %s'%user)

    # Change a user and cheack if it's changed
    logging.debug('Try to change user password')
    userFabio2.password='pwdchg'
    user = session.query(User).filter_by(name='Fabio2').first()
    logging.debug('Retieved user %s'%user)


    logging.info('Test02 end')

if __name__== '__main__':
    main()
