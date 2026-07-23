"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : top_bar.py
Módulo      : UI / Shell
Descripción : Barra superior principal de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QWidget

from src.core.theme_manager import ThemeManager


class TopBar(QFrame):
    """
    Barra superior principal de la aplicación.
    """

    APP_NAME = "FarmaciaPOS"
    APP_VERSION = "v0.1.0"

    def __init__(self) -> None:
        """
        Inicializa la barra superior.
        """
        super().__init__()
        self._initialize_ui()

    @property
    def title_label(self) -> QLabel:
        """
        Retorna el título de la aplicación.
        """
        return self._title_label

    @property
    def version_label(self) -> QLabel:
        """
        Retorna la versión de la aplicación.
        """
        return self._version_label

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz de la barra superior.
        """
        self.setFixedHeight(68)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {ThemeManager.SURFACE_COLOR};
                border-bottom: 1px solid {ThemeManager.BORDER_COLOR};
            }}
            """)

        self._title_label = QLabel("💊  " + self.APP_NAME)
        self._title_label.setStyleSheet(f"""
            QLabel {{
                color: {ThemeManager.TEXT_PRIMARY};
                font-size: 18px;
                font-weight: 700;
                border: none;
                background: transparent;
            }}
            """)

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("Buscar en FarmaciaPOS...")
        self._search_input.setFixedWidth(280)
        self._search_input.setStyleSheet("padding: 8px 12px;")

        self._version_label = QLabel(self.APP_VERSION + "  •  Sesión activa")
        self._version_label.setAlignment(Qt.AlignCenter)
        self._version_label.setStyleSheet(f"""
            QLabel {{
                color: {ThemeManager.TEXT_SECONDARY};
                font-size: 12px;
                border: none;
                background: transparent;
            }}
            """)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 0, 28, 0)
        layout.setSpacing(12)

        layout.addWidget(self._title_label)
        layout.addWidget(spacer)
        layout.addWidget(self._search_input)
        layout.addWidget(self._version_label)

        self.setLayout(layout)
