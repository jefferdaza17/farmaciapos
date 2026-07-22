"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : page.py
Módulo      : Dashboard
Descripción : Página principal del sistema.

Autor       : Jefferson Castellanos
Creado      : 2026-07-22
Python      : 3.13
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.core.constants import APP_NAME, APP_VERSION


class DashboardPage(QWidget):
    """
    Página principal de la aplicación.
    """

    def __init__(self) -> None:
        super().__init__()
        self._create_ui()

    # -------------------------------------------------------------------------
    # Construcción de la interfaz
    # -------------------------------------------------------------------------

    def _create_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel(APP_NAME)
        title.setObjectName("pageTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel(
            f"Versión {APP_VERSION}\n\nBienvenido a FarmaciaPOS"
        )
        subtitle.setObjectName("pageSubtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()