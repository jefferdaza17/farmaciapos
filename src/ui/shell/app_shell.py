"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : app_shell.py
Módulo      : UI / Shell
Descripción : Contenedor principal de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from src.ui.shell.top_bar import TopBar
from src.ui.shell.workspace import Workspace


class AppShell(QWidget):
    """
    Contenedor principal de la interfaz de usuario.
    """

    def __init__(self) -> None:
        """
        Inicializa el contenedor principal.
        """
        super().__init__()
        self._initialize_ui()

    @property
    def top_bar(self) -> TopBar:
        """
        Retorna la barra superior.
        """
        return self._top_bar

    @property
    def workspace(self) -> Workspace:
        """
        Retorna el área de trabajo principal.
        """
        return self._workspace

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz principal.
        """
        self._top_bar = TopBar()
        self._workspace = Workspace()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(self._top_bar)
        main_layout.addWidget(self._workspace, 1)

        self.setLayout(main_layout)