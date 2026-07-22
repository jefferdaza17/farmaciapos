import sys
from PySide6.QtWidgets import QApplication
from src.ui.windows.main_window import MainWindow

class App:
    """
    Punto de entrada de FarmaciaPOS.
    """
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        sys.exit(self.qt_app.exec())
