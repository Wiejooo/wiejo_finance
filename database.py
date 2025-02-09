from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///finance.db"
engine = create_engine(DATABASE_URL, echo=True) # ech pokazuje zapytania sql w terminalu

SessionLocal = sessionmaker(bind=engine)