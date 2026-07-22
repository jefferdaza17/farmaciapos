"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : app_shell.py
Módulo      : UI / Shell
Descripción : Contenedor principal de la interfaz.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
Python      : 3.13
===============================================================================
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

from src.ui.layout.content_area import ContentArea
from src.ui.layout.sidebar import Sidebar


class AppShell(QWidget):
    """
    Contenedor principal de la interfaz.

    Organiza todos los elementos visibles de la aplicación.
    """

    def __init__(self) -> None:
        super().__init__()
        self._create_ui()

    # -------------------------------------------------------------------------
    # Construcción de la interfaz
    # -------------------------------------------------------------------------

    def _create_ui(self) -> None:
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self._sidebar = Sidebar()

        right_container = QWidget()

        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        self._content_area = ContentArea()

        right_layout.addWidget(self._content_area)

        main_layout.addWidget(self._sidebar)
        main_layout.addWidget(right_container, 1)