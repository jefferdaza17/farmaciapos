"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : application.py
Módulo      : Core
Descripción : Inicializa y ejecuta la aplicación principal.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

import sys
from PySide6.QtWidgets import QApplication
from src.ui.windows.main_window import MainWindow
from src.core.theme_manager import ThemeManager

class Application:
    """
    Clase responsable de inicializar y ejecutar la aplicación.
    """

    def __init__(self) -> None:
        """
        Inicializa la aplicación Qt y crea la ventana principal.
        """
        self._qt_application = QApplication(sys.argv)
        ThemeManager.apply(self._qt_application)
        self._main_window = MainWindow()

    @property
    def qt_application(self) -> QApplication:
        """
        Retorna la instancia de QApplication.
        """
        return self._qt_application

    @property
    def main_window(self) -> MainWindow:
        """
        Retorna la ventana principal.
        """
        return self._main_window

    def run(self) -> None:
        """
        Inicia el ciclo principal de la aplicación.
        """
        self._main_window.show()
        sys.exit(self._qt_application.exec())