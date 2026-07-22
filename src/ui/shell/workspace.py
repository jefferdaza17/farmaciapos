"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : workspace.py
Módulo      : UI / Shell
Descripción : Área principal donde se mostrarán los módulos de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from src.core.theme_manager import ThemeManager


class Workspace(QWidget):
    """
    Área principal donde se visualizarán los módulos de FarmaciaPOS.
    """

    def __init__(self) -> None:
        """
        Inicializa el área de trabajo.
        """
        super().__init__()
        self._initialize_ui()

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

        self._title_label = QLabel("Bienvenido a FarmaciaPOS")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setStyleSheet(
            f"""
            QLabel {{
                font-size: 28px;
                font-weight: 700;
                color: {ThemeManager.TEXT_PRIMARY};
                background: transparent;
                border: none;
            }}
            """
        )

        self._subtitle_label = QLabel(
            "Sistema moderno de administración de farmacias"
        )
        self._subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._subtitle_label.setStyleSheet(
            f"""
            QLabel {{
                font-size: 14px;
                color: {ThemeManager.TEXT_SECONDARY};
                background: transparent;
                border: none;
            }}
            """
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(12)

        layout.addStretch()
        layout.addWidget(self._title_label)
        layout.addWidget(self._subtitle_label)
        layout.addStretch()

        self.setLayout(layout)

    @property
    def title_label(self) -> QLabel:
        """
        Retorna el título principal.
        """
        return self._title_label

    @property
    def subtitle_label(self) -> QLabel:
        """
        Retorna el subtítulo.
        """
        return self._subtitle_label