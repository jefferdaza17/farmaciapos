"""
=========================================================
FarmaciaPOS

Archivo:
    main_window.py

Descripción:
    Ventana principal de la aplicación.

=========================================================
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    """
    Ventana principal de FarmaciaPOS.
    """
    def __init__(self):
        super().__init__()
        self._configure_window()
        self._create_ui()

    def _configure_window(self) -> None:
        """Configura la ventana principal."""
        self.setWindowTitle("FarmaciaPOS")
        self.resize(1400, 900)
        self.setMinimumSize(1200, 700)

    def _create_ui(self) -> None:
        """Construye la interfaz principal."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        central_widget.setLayout(layout)
        title = QLabel("Bienvenido a FarmaciaPOS")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")
        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()