"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : navigation_button.py
Módulo      : UI / Components
Descripción : Botón reutilizable para la navegación lateral.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
Python      : 3.13
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    """
    Botón reutilizable para el menú de navegación.
    """

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self._configure()

    # -------------------------------------------------------------------------
    # Configuración
    # -------------------------------------------------------------------------

    def _configure(self) -> None:
        """
        Configura las propiedades visuales del botón.
        """
        self.setObjectName("navigationButton")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(46)
        self.setCheckable(True)