# Inizializzazine modulo models
# come indicato in http://docs.sqlalchemy.org/en/latest/orm/session_basics.html
# Sembra che il modo corretto di gestire la sessione sia
# definirla in un modulo e per poi eseguire un bind
# nel programma di utilizzo con sessionmaker.configure(bind=engine)
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
