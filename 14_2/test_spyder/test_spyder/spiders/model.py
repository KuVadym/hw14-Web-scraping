from datetime import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table


Base = declarative_base()


quote_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("quote", Integer, ForeignKey("quotes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=False)


class Autors(Base):
    __tablename__ = "autors"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description_linc = Column(String(150), nullable=False)
    quotes = relationship("Quote", cascade="all, delete", backref="author")
    autors_info = relationship("AutorsInfo", cascade="all, delete", backref="author_info")

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey(Autors.id, ondelete="CASCADE"))
    tags = relationship("Tag", secondary=quote_m2m_tag, backref="quote")


class AutorsInfo(Base):
    __tablename__ = "autors_info"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    birthdate = Column(String(30), nullable=False)
    birthplace = Column(String(30), nullable=False)
    description = Column(String(1500), nullable=False)
    author_id = Column(Integer, ForeignKey(Autors.id, ondelete="CASCADE"))