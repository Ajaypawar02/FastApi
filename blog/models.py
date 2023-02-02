from sqlalchemy import Column, Integer, String
# from database import Base
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

class Blog(Base):

    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String)
    body = Column(String)

