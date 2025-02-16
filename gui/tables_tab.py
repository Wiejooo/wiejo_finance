from PyQt6 import QtWidgets as Qt
from core import get_all_from_table

class TablesTab(Qt.QWidget):
    def __init__(self):
        super().__init__()
    
        page = Qt.QWidget()
        layout = Qt.QVBoxLayout()

        # Tworzy Layout tabel
        tables_layout = Qt.QHBoxLayout()

        # Tworzy tabele
        self.bonds_table = Qt.QTableWidget()
        self.shares_table = Qt.QTableWidget()

        # Dodaje tabele do layoutu tabel
        tables_layout.addWidget(self.bonds_table)
        tables_layout.addWidget(self.shares_table)

        # Dodaje layout tabel to lauoutu głównego
        layout.addLayout(tables_layout)
        page.setLayout(layout)

        # Wypełnienie tabel
        self.load_bonds()
        self.load_shares()

        self.setLayout(layout)

    def load_bonds(self):
        # Obligacje
        bonds_table = get_all_from_table('Bonds')
        self.bonds_table.setRowCount(len(bonds_table))
        self.bonds_table.setColumnCount(4)
        self.bonds_table.setHorizontalHeaderLabels(["Nazwa", "Cena zakupu", "Data zakupu", "Kod"])
        for row, bond in enumerate(bonds_table):
            self.bonds_table.setItem(row, 0, Qt.QTableWidgetItem(bond.name))
            self.bonds_table.setItem(row, 1, Qt.QTableWidgetItem(str(bond.purchase_price)))
            self.bonds_table.setItem(row, 2, Qt.QTableWidgetItem(str(bond.purchase_date)))
            self.bonds_table.setItem(row, 3, Qt.QTableWidgetItem(str(bond.code)))

    def load_shares(self):
        self.shares_table.clearContents()
        # Akcje
        shares_table = get_all_from_table("Shares")
        self.shares_table.setRowCount(len(shares_table))
        self.shares_table.setColumnCount(4)
        self.shares_table.setHorizontalHeaderLabels(["Nazwa", "Cena zakupu", "Data zakupu", "Kod"])
        for row, share in enumerate(shares_table):
            self.shares_table.setItem(row, 0, Qt.QTableWidgetItem(share.name))
            self.shares_table.setItem(row, 1, Qt.QTableWidgetItem(str(share.purchase_price)))
            self.shares_table.setItem(row, 2, Qt.QTableWidgetItem(str(share.purchase_date)))
            self.shares_table.setItem(row, 3, Qt.QTableWidgetItem(str(share.code)))
    