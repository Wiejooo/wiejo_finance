from PyQt6 import QtWidgets as Qt
from PyQt6.QtCore import QTimer
from core import get_all_from_table, add_shares


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wiejo Finance")
        self.setGeometry(100, 100, 1000, 700)

        # Tworzymy QTabWidget (zakładki)
        self.tabs = Qt.QTabWidget()
        self.setCentralWidget(self.tabs)

        # Tworzenie zakładek
        self.page1 = self.create_table_page()
        self.page2 = self.operation_page()

        # Dodanie zakładek do QTabWidget
        self.tabs.addTab(self.page1, "Tabela Bonds & Shares")
        self.tabs.addTab(self.page2, "Operacje")

        # Ładowanie danych
        self.load_bonds()
        self.load_shares()

    def handle_add_shares(self):
        """Obsługa dodawania akcji"""
        name = self.name_input.text()
        purchase_price = float(self.purchase_price.text())
        purchase_date = self.purchase_date.date().toPyDate()
        add_shares(name, purchase_price, purchase_date)

    def create_table_page(self):
        """Tworzy stronę z tabelami"""
        page = Qt.QWidget()
        layout = Qt.QVBoxLayout()

        # Layout dla tabel
        tables_layout = Qt.QHBoxLayout()
        self.bonds_table = Qt.QTableWidget()
        self.shares_table = Qt.QTableWidget()

        tables_layout.addWidget(self.bonds_table)
        tables_layout.addWidget(self.shares_table)

        layout.addLayout(tables_layout)
        page.setLayout(layout)

        # Wypełnienie tabel
        self.load_bonds()
        self.load_shares()

        return page

    def operation_page(self):
        """Strona do operacji"""
        page = Qt.QWidget()
        layout = Qt.QVBoxLayout()

        # Losowy tekst
        label = Qt.QLabel('Dodaj akcje')
        layout.addWidget(label)

        # Stworzenie formularza
        form_layout = Qt.QFormLayout()
        self.name_input = Qt.QLineEdit()
        self.purchase_price = Qt.QLineEdit()
        self.purchase_date = Qt.QDateEdit()
        self.purchase_date.setCalendarPopup(True)

        form_layout.addRow("Nazwa:", self.name_input)
        form_layout.addRow("Koszt:", self.purchase_price)
        form_layout.addRow("Data:", self.purchase_date)

        # Dodanie formularza do layout
        layout.addLayout(form_layout)

        # Stworzenie przycisku
        submit_button = Qt.QPushButton("Dodaj akcję")
        submit_button.clicked.connect(self.handle_add_shares)
        submit_button.clicked.connect(self.load_shares) # Jeśli rekord się nie pojawi to load_shares wykonało się przed handle_add_shares
        

        # Dodanie przycisku do layout
        layout.addWidget(submit_button)

        # Dodanie layout do strony
        page.setLayout(layout)

        return page

    def load_bonds(self):
        # Obligacje
        bonds_table = get_all_from_table('Bonds') 
        self.bonds_table.setRowCount(len(bonds_table))
        self.bonds_table.setColumnCount(4)
        self.bonds_table.setHorizontalHeaderLabels(["Kod", "Nazwa", "Cena zakupu", "Data zakupu"])
        for row, bond in enumerate(bonds_table):
            self.bonds_table.setItem(row, 0, Qt.QTableWidgetItem(bond.name))
            self.bonds_table.setItem(row, 1, Qt.QTableWidgetItem(str(bond.purchase_price)))
            self.bonds_table.setItem(row, 2, Qt.QTableWidgetItem(str(bond.purchase_date)))
            self.bonds_table.setItem(row, 3, Qt.QTableWidgetItem(str(bond.code)))

    def load_shares(self):
        # Akcje
        shares_table = get_all_from_table("Shares")
        self.shares_table.setRowCount(len(shares_table))
        self.shares_table.setColumnCount(4)
        self.shares_table.setHorizontalHeaderLabels(["Kod", "Nazwa", "Cena zakupu", "Data zakupu"])
        for row, share in enumerate(shares_table):
            self.shares_table.setItem(row, 0, Qt.QTableWidgetItem(share.name))
            self.shares_table.setItem(row, 1, Qt.QTableWidgetItem(str(share.purchase_price)))
            self.shares_table.setItem(row, 2, Qt.QTableWidgetItem(str(share.purchase_date)))
            self.shares_table.setItem(row, 3, Qt.QTableWidgetItem(str(share.code)))


if __name__ == "__main__":
    app = Qt.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()