from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Organizations_db(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
