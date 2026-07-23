"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : home_page.py
Módulo      : Modules / Home
Descripción : Página principal de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from src.core.theme_manager import ThemeManager


class HomePage(QWidget):
    """
    Página de inicio.
    """

    def __init__(self) -> None:
        """
        Inicializa la página.
        """
        super().__init__()
        self._initialize_ui()

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz.
        """
        title = QLabel("Inicio")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet(
            f"""
            QLabel {{
                font-size:32px;
                font-weight:700;
                color:{ThemeManager.TEXT_PRIMARY};
            }}
            """
        )

        subtitle = QLabel("Bienvenido a FarmaciaPOS")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle.setStyleSheet(
            f"""
            QLabel {{
                font-size:16px;
                color:{ThemeManager.TEXT_SECONDARY};
            }}
            """
        )

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()