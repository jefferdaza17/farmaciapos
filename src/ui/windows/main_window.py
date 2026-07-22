"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : main_window.py
Módulo      : UI / Windows
Descripción : Ventana principal de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
Python      : 3.13
===============================================================================
"""

from PySide6.QtWidgets import QMainWindow

from src.core.constants import APP_NAME
from src.ui.shell.app_shell import AppShell


class MainWindow(QMainWindow):
    """
    Ventana principal de FarmaciaPOS.
    """

    def __init__(self) -> None:
        super().__init__()
        self._configure_window()
        self._create_ui()

    # -------------------------------------------------------------------------
    # Configuración
    # -------------------------------------------------------------------------

    def _configure_window(self) -> None:
        self.setWindowTitle(APP_NAME)
        self.resize(1400, 900)
        self.setMinimumSize(1200, 700)

    # -------------------------------------------------------------------------
    # Construcción de la interfaz
    # -------------------------------------------------------------------------

    def _create_ui(self) -> None:
        self.setCentralWidget(AppShell())