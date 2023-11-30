import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

    #---HEROKU DATABASE ----

_hostname = 'sour-hawthorn.db.elephantsql.com'
_username = 'wficixke'
_password = 'pdeYA4t0t2psZcZL87t6zPjNpNQ5e0Jt'
_database = 'millerdb' 

DATABASE_URL = "postgresql://"+_username + ":"+ _password +"@"+ _hostname +":5432/" + _database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


def conn():
    conn = psycopg2.connect(host=_hostname ,
                    user=_username,
                    password=_password,
                    database=_database)
    return conn