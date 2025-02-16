# from PyQt6 import QtWidgets as Qt
# from core import get_all_from_table, add_share, add_bond


# class MainWindow(Qt.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Wiejo Finance")
#         self.setGeometry(100, 100, 1000, 700)

#         # Tworzymy QTabWidget (zakładki)
#         self.tabs = Qt.QTabWidget()
#         self.setCentralWidget(self.tabs)

#         # Tworzenie zakładek
#         self.page1 = self.create_table_page()
#         self.page2 = self.operation_page()

#         # Dodanie zakładek do QTabWidget
#         self.tabs.addTab(self.page1, "Tabela Bonds & Shares")
#         self.tabs.addTab(self.page2, "Operacje")

#     def handle_add_share(self):
#         """Obsługa dodawania akcji"""
#         name = self.name_input.text()
#         purchase_price = float(self.purchase_price.text())
#         purchase_date = self.purchase_date.date().toPyDate()
#         add_share(name, purchase_price, purchase_date)

#     def handle_add_bond(self):
#         """Obsługa dodawania obligacji"""
#         name = self.bond_name_input.text()
#         purchase_price = float(self.bond_purchase_price.text())
#         purchase_date = self.bond_purchase_date.date().toPyDate()
#         add_bond(name, purchase_price, purchase_date)

#     def create_table_page(self):
#         """Tworzy stronę z tabelami"""
#         page = Qt.QWidget()
#         layout = Qt.QVBoxLayout()

#         # Tworzy Layout tabel
#         tables_layout = Qt.QHBoxLayout()

#         # Tworzy tabele
#         self.bonds_table = Qt.QTableWidget()
#         self.shares_table = Qt.QTableWidget()

#         # Dodaje tabele do layoutu tabel
#         tables_layout.addWidget(self.bonds_table)
#         tables_layout.addWidget(self.shares_table)

#         # Dodaje layout tabel to lauoutu głównego
#         layout.addLayout(tables_layout)
#         page.setLayout(layout)

#         # Wypełnienie tabel
#         self.load_bonds()
#         self.load_shares()

#         return page

#     def operation_page(self):
#         """Tworzy strone z operacji"""
#         page = Qt.QWidget()
#         layout = Qt.QVBoxLayout()

#         # Tworzenie tekstu dla akcji
#         label_shares = Qt.QLabel('Dodaj akcje')
#         layout.addWidget(label_shares)

#         # Stworzenie formularza
#         form_layout = Qt.QFormLayout()
#         self.name_input = Qt.QLineEdit()
#         self.purchase_price = Qt.QLineEdit()
#         self.purchase_date = Qt.QDateEdit()
#         self.purchase_date.setCalendarPopup(True)

#         form_layout.addRow("Nazwa:", self.name_input)
#         form_layout.addRow("Koszt:", self.purchase_price)
#         form_layout.addRow("Data:", self.purchase_date)

#         # Dodanie formularza do layout
#         layout.addLayout(form_layout)

#         # Stworzenie przycisku
#         submit_button = Qt.QPushButton("Dodaj akcję")
#         submit_button.clicked.connect(self.handle_add_share)
#         submit_button.clicked.connect(self.load_shares) # Jeśli rekord się nie pojawi to load_shares wykonało się przed handle_add_shares
        

#         # Dodanie przycisku do layout
#         layout.addWidget(submit_button)

#         # Tworzenie tekstu dla obligacji
#         label_bonds = Qt.QLabel('Dodaj obligacje')
#         layout.addWidget(label_bonds)

#         # Stworzenie formularza
#         form_layout_bonds = Qt.QFormLayout()
#         self.bond_name_input = Qt.QLineEdit()
#         self.bond_purchase_price = Qt.QLineEdit()
#         self.bond_purchase_date = Qt.QDateEdit()
#         self.bond_purchase_date.setCalendarPopup(True)

#         form_layout_bonds.addRow("Nazwa:", self.bond_name_input)
#         form_layout_bonds.addRow("Koszt:", self.bond_purchase_price)
#         form_layout_bonds.addRow("Data:", self.bond_purchase_date)

#         # Dodanie formularza do layout
#         layout.addLayout(form_layout_bonds)

#         # Stworzenie przycisku
#         bond_submit_button = Qt.QPushButton("Dodaj obligacje")
#         bond_submit_button.clicked.connect(self.handle_add_bond)
#         bond_submit_button.clicked.connect(self.load_bonds)

#         # Dodanie przycisku do layout
#         layout.addWidget(bond_submit_button)

#         # Dodanie layout do strony
#         page.setLayout(layout)

#         return page

#     def load_bonds(self):
#         # Obligacje
#         bonds_table = get_all_from_table('Bonds') 
#         self.bonds_table.setRowCount(len(bonds_table))
#         self.bonds_table.setColumnCount(4)
#         self.bonds_table.setHorizontalHeaderLabels(["Nazwa", "Cena zakupu", "Data zakupu", "Kod"])
#         for row, bond in enumerate(bonds_table):
#             self.bonds_table.setItem(row, 0, Qt.QTableWidgetItem(bond.name))
#             self.bonds_table.setItem(row, 1, Qt.QTableWidgetItem(str(bond.purchase_price)))
#             self.bonds_table.setItem(row, 2, Qt.QTableWidgetItem(str(bond.purchase_date)))
#             self.bonds_table.setItem(row, 3, Qt.QTableWidgetItem(str(bond.code)))

#     def load_shares(self):
#         # Akcje
#         shares_table = get_all_from_table("Shares")
#         self.shares_table.setRowCount(len(shares_table))
#         self.shares_table.setColumnCount(4)
#         self.shares_table.setHorizontalHeaderLabels(["Nazwa", "Cena zakupu", "Data zakupu", "Kod"])
#         for row, share in enumerate(shares_table):
#             self.shares_table.setItem(row, 0, Qt.QTableWidgetItem(share.name))
#             self.shares_table.setItem(row, 1, Qt.QTableWidgetItem(str(share.purchase_price)))
#             self.shares_table.setItem(row, 2, Qt.QTableWidgetItem(str(share.purchase_date)))
#             self.shares_table.setItem(row, 3, Qt.QTableWidgetItem(str(share.code)))


# if __name__ == "__main__":
#     app = Qt.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()