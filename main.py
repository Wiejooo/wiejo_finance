from database import engine
from models import Base
from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication


Base.metadata.create_all(engine)

if __name__ == "__main__":
    app = QApplication([]) # Główna pętla
    window = MainWindow() # Tworzy główne okno
    window.show() # Pokazuje główne okno
    app.exec() # Czeka na zdarzenie użytkownika