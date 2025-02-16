from database import SessionLocal
from models import Bonds, Shares

session = SessionLocal() # Stworzenie sesji, odpowiedzialnej za komunikacje z bazą danych

def add_bond(name:str, purchase_price:int, purchase_date:dict):
    # Stworzenie obiektu
    new_bond = Bonds(
        name=name,
        purchase_price=purchase_price,
        purchase_date=purchase_date
    )
    # Dodanie do sesji
    session.add(new_bond)
    # Zatwierdzenie zmian w bazie
    session.commit()

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


def add_share(name:str, purchase_price:int, purchase_date):
    # Stworzenie obiektu
    new_share = Shares(
        name=name,
        purchase_price=purchase_price,
        purchase_date=purchase_date
    )
    # Dodanie do sesji
    session.add(new_share)
    # Zatwierdzenie zmian w bazie
    session.commit()

def delete_share(id:int):
    share_to_delete = session.query(Shares).filter(Shares.id == id).first()
    share_name = share_to_delete.name
    if share_to_delete:
        # Usunięcie obiektu
        session.delete(share_to_delete)
        # Zatwierdzenie zmian w bazie
        session.commit()
        print(f'Akcja {share_name}, została usunięta')
    else:
        print(f'Akcja o id {id}, nie została znaleziona')

def get_all_from_table(table):
    """Pobiera z bazy wszystkie rekordy"""
    tables = {
        'Bonds': Bonds,
        'Shares': Shares
        }
    return session.query(tables[table]).all()
