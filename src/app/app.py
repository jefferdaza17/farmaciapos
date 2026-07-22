import sys
from PySide6.QtWidgets import QApplication
from src.core.theme import ThemeManager
from src.ui.windows.main_window import MainWindow


class App:
    def __init__(self) -> None:
        self.qt_app = QApplication(sys.argv)
        ThemeManager.load(self.qt_app)
        self.window = MainWindow()

    def run(self) -> None:
        self.window.show()
        sys.exit(self.qt_app.exec())