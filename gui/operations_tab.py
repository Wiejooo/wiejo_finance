from PyQt6 import QtWidgets as Qt
from core import add_share, add_bond

class OperationsTab(Qt.QWidget):
    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout()

        # Formularz dla akcji
        label_shares = Qt.QLabel('Dodaj akcje')
        layout.addWidget(label_shares)

        form_layout = Qt.QFormLayout()
        self.name_input = Qt.QLineEdit()
        self.purchase_price = Qt.QLineEdit()
        self.purchase_date = Qt.QDateEdit()
        self.purchase_date.setCalendarPopup(True)

        form_layout.addRow("Nazwa:", self.name_input)
        form_layout.addRow("Koszt:", self.purchase_price)
        form_layout.addRow("Data:", self.purchase_date)

        layout.addLayout(form_layout)

        submit_button = Qt.QPushButton("Dodaj akcję")
        submit_button.clicked.connect(self.handle_add_share)

        layout.addWidget(submit_button)

        # Formularz dla obligacji
        label_bonds = Qt.QLabel('Dodaj obligacje')
        layout.addWidget(label_bonds)

        form_layout_bonds = Qt.QFormLayout()
        self.bond_name_input = Qt.QLineEdit()
        self.bond_purchase_price = Qt.QLineEdit()
        self.bond_purchase_date = Qt.QDateEdit()
        self.bond_purchase_date.setCalendarPopup(True)

        form_layout_bonds.addRow("Nazwa:", self.bond_name_input)
        form_layout_bonds.addRow("Koszt:", self.bond_purchase_price)
        form_layout_bonds.addRow("Data:", self.bond_purchase_date)

        layout.addLayout(form_layout_bonds)

        bond_submit_button = Qt.QPushButton("Dodaj obligacje")
        bond_submit_button.clicked.connect(self.handle_add_bond)

        layout.addWidget(bond_submit_button)

        self.setLayout(layout)

    def handle_add_share(self):
        """Obsługa dodawania akcji"""
        name = self.name_input.text()
        purchase_price = float(self.purchase_price.text())
        purchase_date = self.purchase_date.date().toPyDate()
        add_share(name, purchase_price, purchase_date)

    def handle_add_bond(self):
        """Obsługa dodawania obligacji"""
        name = self.bond_name_input.text()
        purchase_price = float(self.bond_purchase_price.text())
        purchase_date = self.bond_purchase_date.date().toPyDate()
        add_bond(name, purchase_price, purchase_date)
