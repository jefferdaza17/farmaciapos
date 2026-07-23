"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : workspace.py
Módulo      : UI / Shell
Descripción : Contenedor principal de páginas de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from src.core.theme_manager import ThemeManager


class Workspace(QWidget):
    """
    Contenedor encargado de administrar las páginas de la aplicación.
    """

    def __init__(self) -> None:
        """
        Inicializa el Workspace.
        """
        super().__init__()
        self._initialize_ui()

    @property
    def stacked_widget(self) -> QStackedWidget:
        """
        Retorna el contenedor de páginas.
        """
        return self._stacked_widget

    def add_page(self, page: QWidget) -> None:
        """
        Agrega una nueva página al Workspace.
        """
        self._stacked_widget.addWidget(page)

    def set_current_page(self, page: QWidget) -> None:
        """
        Establece la página activa.
        """
        self._stacked_widget.setCurrentWidget(page)

    def current_page(self) -> QWidget:
        """
        Retorna la página actualmente visible.
        """
        return self._stacked_widget.currentWidget()

    def page_count(self) -> int:
        """
        Retorna la cantidad de páginas registradas.
        """
        return self._stacked_widget.count()

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz del Workspace.
        """
        self.setObjectName("workspace")

        self.setStyleSheet(
            f"""
            QWidget#workspace {{
                background-color: {ThemeManager.BACKGROUND_COLOR};
            }}
            """
        )

        self._stacked_widget = QStackedWidget()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._stacked_widget)

        self.setLayout(layout)