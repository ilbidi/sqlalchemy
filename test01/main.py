import logging
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

def main():
    # Configure logging
    logging.basicConfig(filename='main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # Start program
    logging.info('Test01 start')
    # Display SqlAlchemy version
    logging.debug('SqlAlchemy version : %s.'%sqlalchemy.__version__)

    logging.debug('Connect to db')
    engine = create_engine('sqlite:///:memory:', echo=True)

    logging.debug('Create a declarative base')
    Base = declarative_base()

    logging.debug('Create a table Users')
    class User(Base):
    	__tablename__ = 'users'
    	id = Column(Integer, primary_key = True)
    	name = Column(String)
    	fullname = Column(String)
    	password = Column(String)
    	def __repr__(self):
    		return '<User(''name''=%s, ''fullname''=%s, ''password''=%s)>' % ( self.name, self.fullname, self.password)
    
    logging.debug('Crete metadata')
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
    userFabio2.password='pwdchg'
    user = session.query(User).filter_by(name='Fabio2').first()
    logging.debug('Retieved user %s'%user)

    
    logging.info('Test01 end')

if __name__== '__main__':
    main()
