from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout

from core import get_all_from_table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wiejo Finance")
        self.setGeometry(100, 100, 800, 600)

        # Storzenie głównego widgetu
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouty
        main_layout = QVBoxLayout()
        tables_layout = QHBoxLayout()

        # Tworzenie tabel
        self.bonds_table = QTableWidget()
        self.shares_table = QTableWidget()

        tables_layout.addWidget(self.bonds_table)
        tables_layout.addWidget(self.shares_table)

        main_layout.addLayout(tables_layout)
        central_widget.setLayout(main_layout)

        # Ładowanie danych
        self.load_bonds()
        self.load_shares()

    def load_bonds(self):
        # Obligacje
        bonds_table = get_all_from_table('Bonds') 
        self.bonds_table.setRowCount(len(bonds_table))
        self.bonds_table.setColumnCount(4)
        self.bonds_table.setHorizontalHeaderLabels(["Kod", "Nazwa", "Cena zakupu", "Data zakupu"])
        for row, bond in enumerate(bonds_table):
            self.bonds_table.setItem(row, 0, QTableWidgetItem(bond.name))
            self.bonds_table.setItem(row, 1, QTableWidgetItem(str(bond.purchase_price)))
            self.bonds_table.setItem(row, 2, QTableWidgetItem(str(bond.purchase_date)))
            self.bonds_table.setItem(row, 3, QTableWidgetItem(str(bond.code)))

    def load_shares(self):
        # Akcje
        shares_table = get_all_from_table("Shares")
        self.shares_table.setRowCount(len(shares_table))
        self.shares_table.setColumnCount(4)
        self.shares_table.setHorizontalHeaderLabels(["Kod", "Nazwa", "Cena zakupu", "Data zakupu"])
        for row, share in enumerate(shares_table):
            self.shares_table.setItem(row, 0, QTableWidgetItem(share.name))
            self.shares_table.setItem(row, 1, QTableWidgetItem(str(share.purchase_price)))
            self.shares_table.setItem(row, 2, QTableWidgetItem(str(share.purchase_date)))
            self.shares_table.setItem(row, 3, QTableWidgetItem(str(share.code)))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()