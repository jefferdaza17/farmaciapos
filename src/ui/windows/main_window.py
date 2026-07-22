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
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from src.core.constants import APP_NAME, APP_VERSION

class MainWindow(QMainWindow):
    """
    Ventana principal de FarmaciaPOS.
    """
    def __init__(self) -> None:
        super().__init__()
        self._configure_window()
        self._create_ui()

    # --------------------------------------------------
    # Configuración
    # --------------------------------------------------
    def _configure_window(self) -> None:
        """Configura la ventana principal."""
        self.setWindowTitle(APP_NAME)
        self.resize(1400, 900)
        self.setMinimumSize(1200, 700)

    # --------------------------------------------------
    # UI
    # --------------------------------------------------
    def _create_ui(self) -> None:
        self._central_widget = QWidget()
        self.setCentralWidget(self._central_widget)
        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(40, 40, 40, 40)
        self._main_layout.setSpacing(20)
        self._central_widget.setLayout(self._main_layout)
        self._create_placeholder()

    def _create_placeholder(self) -> None:
        title = QLabel(APP_NAME)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)
        subtitle = QLabel(
            f"Versión {APP_VERSION}\n\nFramework Base Inicializado"
        )
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size:16px;
            color:gray;
        """)
        self._main_layout.addStretch()
        self._main_layout.addWidget(title)
        self._main_layout.addWidget(subtitle)
        self._main_layout.addStretch()