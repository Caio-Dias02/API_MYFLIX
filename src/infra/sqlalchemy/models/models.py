from sqlalchemy.sql.sqltypes import String
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String

class Serie(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    gender = Column(String)
    seasons = Column(Integer)
    size = Column(String)