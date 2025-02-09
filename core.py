from datetime import date
from database import SessionLocal
from models import Bonds, Shares

session = SessionLocal() # Stworzenie sesji, odpowiedzialnej za komunikacje z bazą danych

def add_bond(name:str, purchase_price:int, purchase_date:dict):
    # Stworzenie obiektu
    new_bond = Bonds(
        name=name,
        purchase_price=purchase_price,
        purchase_date=date(purchase_date['year'], purchase_date['month'], purchase_date['day'])
    )
    # Dodanie do sesji
    session.add(new_bond)
    # Zatwierdzenie zmian w bazie
    session.commit()
    print('')

def delete_bond(id:int):
    bond_to_delete = session.query(Bonds).filter(Bonds.id == id).first()
    bond_name = bond_to_delete.name
    if bond_to_delete:
        # Usunięcie obiektu
        session.delete(bond_to_delete)
        # Zatwierdzenie zmian w bazie
        session.commit()
        print(f'Obligacja {bond_name}, została usunięta')
    else:
        print(f'Obligacja o id {id}, nie została znaleziona')


def add_shares(name:str, purchase_price:int, purchase_date:dict):
    # Stworzenie obiektu
    new_share = Shares(
        name=name,
        purchase_price=purchase_price,
        purchase_date=date(purchase_date['year'], purchase_date['month'], purchase_date['day'])
    )
    # Dodanie do sesji
    session.add(new_share)
    # Zatwierdzenie zmian w bazie
    session.commit()
