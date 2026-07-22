"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : main_window.py
Módulo      : UI / Windows
Descripción : Ventana principal de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow
from src.ui.shell.app_shell import AppShell


class MainWindow(QMainWindow):
    """
    Ventana principal de FarmaciaPOS.
    """

    def __init__(self) -> None:
        """
        Inicializa la ventana principal.
        """
        super().__init__()
        self._initialize_window()
        self._initialize_ui()

    def _initialize_window(self) -> None:
        """
        Configura las propiedades generales de la ventana.
        """
        self.setWindowTitle("FarmaciaPOS")
        self.resize(1440, 900)
        self.setMinimumSize(1200, 700)
        self.setWindowState(Qt.WindowMaximized)

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz principal.
        """
        self._app_shell = AppShell()
        self.setCentralWidget(self._app_shell)

    @property
    def app_shell(self) -> AppShell:
        """
        Retorna el contenedor principal de la aplicación.
        """
        return self._app_shell

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        Evento ejecutado antes de cerrar la aplicación.
        """
        event.accept()