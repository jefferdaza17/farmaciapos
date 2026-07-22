"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : content_area.py
Módulo      : UI / Layout
Descripción : Área principal de contenido.

Autor       : Jefferson Castellanos
Creado      : 2026-07-22
Python      : 3.13
===============================================================================
"""
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget
from src.modules.dashboard.page import DashboardPage


class ContentArea(QWidget):
    """
    Área principal donde se muestran los módulos de la aplicación.
    """

    def __init__(self) -> None:
        super().__init__()
        self._create_ui()

    # -------------------------------------------------------------------------
    # Construcción de la interfaz
    # -------------------------------------------------------------------------

    def _create_ui(self) -> None:
        self.setObjectName("contentArea")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self._stack = QStackedWidget()

        self._dashboard = DashboardPage()

        self._stack.addWidget(self._dashboard)

        layout.addWidget(self._stack)