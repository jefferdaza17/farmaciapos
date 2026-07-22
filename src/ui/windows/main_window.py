"""
=========================================================
FarmaciaPOS

Archivo:
    main_window.py

Descripción:
    Ventana principal de la aplicación.

Autor:
    Jefferson Castellanos

=========================================================
"""
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from src.core.constants import APP_NAME
from src.ui.layout.content_area import ContentArea
from src.ui.layout.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Ventana principal de FarmaciaPOS."""

    def __init__(self) -> None:
        super().__init__()
        self._configure_window()
        self._create_ui()

    def _configure_window(self) -> None:
        self.setWindowTitle(APP_NAME)
        self.resize(1400, 900)
        self.setMinimumSize(1200, 700)

    def _create_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._sidebar = Sidebar()
        self._content_area = ContentArea()

        layout.addWidget(self._sidebar)
        layout.addWidget(self._content_area, 1)