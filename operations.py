import core
from datetime import datetime
from models import Shares
from database import SessionLocal

session = SessionLocal()
# date_str = "2025-02-10"
date_str = "10.10.2020"
purchase_date = datetime.strptime(date_str, "%d.%m.%Y").date()
# new_share = Shares(name="Apple", purchase_price=150.5, purchase_date=purchase_date)

print(purchase_date)


# core.add_shares('Apple', 223, purchase_date)
# core.delete_bond(1)