from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Text

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    nation = Column(String, nullable=False)
    profile = relationship("Profile", back_populates="user", uselist=False)
    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")

