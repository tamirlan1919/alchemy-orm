from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import Base

engine = create_engine("sqlite:///database.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

Base.metadata.create_all(engine)

