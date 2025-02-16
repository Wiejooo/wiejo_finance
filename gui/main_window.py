from PyQt6 import QtWidgets as Qt
from gui.operations_tab import OperationsTab
from gui.tables_tab import TablesTab


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wiejo Finance")
        self.setGeometry(100, 100, 1000, 700)

        # Tworzymy QTabWidget (zakładki)
        self.tabs = Qt.QTabWidget()
        self.setCentralWidget(self.tabs)

        # Tworzenie zakładek
        self.tables_tab = TablesTab()
        self.operation_tab = OperationsTab()

        # Dodanie zakładek do QTabWidget
        self.tabs.addTab(self.tables_tab, "Tabela Bonds & Shares")
        self.tabs.addTab(self.operation_tab, "Operacje")

if __name__ == "__main__":
    app = Qt.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()