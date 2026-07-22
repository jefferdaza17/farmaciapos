"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : sidebar.py
Módulo      : UI / Layout
Descripción : Panel lateral de navegación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
Python      : 3.13
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.core.constants import APP_NAME
from src.ui.components.navigation_button import NavigationButton


class Sidebar(QWidget):
    """
    Panel lateral de navegación.
    """

    def __init__(self) -> None:
        super().__init__()
        self._create_ui()

    # -------------------------------------------------------------------------
    # Construcción de la interfaz
    # -------------------------------------------------------------------------

    def _create_ui(self) -> None:
        self.setFixedWidth(260)
        self.setObjectName("sidebar")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        self._create_logo(layout)
        self._create_menu(layout)

        layout.addStretch()

    def _create_logo(self, layout: QVBoxLayout) -> None:
        """
        Construye la sección del logo.
        """
        logo = QLabel("💊")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setObjectName("logo")

        title = QLabel(APP_NAME)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("sidebarTitle")

        layout.addWidget(logo)
        layout.addWidget(title)

    def _create_menu(self, layout: QVBoxLayout) -> None:
        """
        Construye el menú principal.
        """
        buttons = [
            "🏠 Dashboard",
            "💊 Productos",
            "🛒 Ventas",
            "📦 Inventario",
            "👥 Clientes",
            "🚚 Proveedores",
            "💰 Caja",
            "📈 Reportes",
        ]

        for index, text in enumerate(buttons):
            button = NavigationButton(text)
            button.setChecked(index == 0)
            layout.addWidget(button)