from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class WatchTable(Base):
    __tablename__ = 'watch'

    id = Column(Integer, primary_key=True)
    brand = Column(String(20), unique=True)
    price = Column(Integer)
    colour = Column(String(20))

    def __repr__(self):
        return f"id: {self.id}, brand: {self.brand}"

