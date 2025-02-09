import uuid
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from database import SessionLocal

Base = declarative_base()
session = SessionLocal()


class Shares(Base):
    """Obiekt akcji"""
    __tablename__ = "Shares"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(Date, nullable=False)
    code = Column(String, unique=True, nullable=False)

    def __init__(self, name, purchase_price, purchase_date):
        self.name = name
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.code = self.generate_unique_code()

    def generate_unique_code(self):
        """Generator unikalnego kodu"""
        while True:
            generated_code = str(uuid.uuid4())
            if not self.code_exists(generated_code):
                return generated_code
    
    def code_exists(self, code):
        """Sprawdzenie czy kod już isnieje w bazie"""
        existing_instrument = session.query(Shares).filter(Shares.code == code).first()
        return existing_instrument is not None


class Bonds(Base):
    """Obiekt obligacji"""
    __tablename__ = "Bonds"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(Date, nullable=False)
    code = Column(String, unique=True, nullable=False)

    def __init__(self, name, purchase_price, purchase_date):
        self.name = name
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.code = self.generate_unique_code()

    def generate_unique_code(self):
        """Generator unikalnego kodu"""
        while True:
            generated_code = str(uuid.uuid4())
            if not self.code_exists(generated_code):
                return generated_code
    
    def code_exists(self, code):
        """Sprawdzenie czy kod już isnieje w bazie"""
        existing_instrument = session.query(Bonds).filter(Bonds.code == code).first()
        return existing_instrument is not None