from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    from local import connection_string 
except:
    pass

#connect you you db here
engine = create_engine(connection_string)
session = sessionmaker(bind=engine)()
engine.connect()

from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float

Base = declarative_base()

class ErcotLMP(Base):
    
    __tablename__ = 'ErcotLMP'

    id = Column(Integer, primary_key=True)
    settlement_point = Column(String(30))
    lmp = Column(Float)
    five_min = Column(Float)