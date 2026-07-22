"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : navigation_button.py
Módulo      : UI / Components
Descripción : Botón reutilizable para el menú lateral.

Autor       : Jefferson Castellanos
Creado      : 2026-07-22
Python      : 3.13
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    """
    Botón reutilizable del menú lateral.
    """

    def __init__(self, text: str, icon: QIcon) -> None:
        super().__init__(text)
        self._configure(icon)

    # -------------------------------------------------------------------------
    # Configuración
    # -------------------------------------------------------------------------

    def _configure(self, icon: QIcon) -> None:
        self.setObjectName("navigationButton")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setCheckable(True)
        self.setMinimumHeight(46)
        self.setIcon(icon)
        self.setIconSize(self.iconSize())