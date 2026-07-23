"""
===============================================================================
Proyecto    : FarmaciaPOS
Archivo     : launcher.py
Módulo      : UI / Shell
Descripción : Panel lateral de navegación de la aplicación.

Autor       : Jefferson Castellanos
Creado      : 2026-07-21
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout

from src.core.router import Router
from src.core.theme_manager import ThemeManager
from src.core.workspace_registry import WorkspaceRegistry


class Launcher(QFrame):
    """
    Panel lateral encargado de mostrar los módulos registrados.
    """

    def __init__(
        self,
        registry: WorkspaceRegistry,
        router: Router
    ) -> None:
        """
        Inicializa el Launcher.
        """
        super().__init__()

        self._registry = registry
        self._router = router
        self._buttons: dict[str, QPushButton] = {}

        self._initialize_ui()

    @property
    def buttons(self) -> dict[str, QPushButton]:
        """
        Retorna los botones registrados.
        """
        return self._buttons

    def refresh(self) -> None:
        """
        Reconstruye el menú de navegación.
        """
        while self._layout.count():
            item = self._layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

        self._buttons.clear()

        self._build_menu()

    def _initialize_ui(self) -> None:
        """
        Construye la interfaz.
        """
        self.setObjectName("launcher")
        self.setFixedWidth(220)

        self.setStyleSheet(
            f"""
            QFrame#launcher {{
                background-color: {ThemeManager.SURFACE_COLOR};
                border-right: 1px solid {ThemeManager.BORDER_COLOR};
            }}

            QPushButton {{
                background-color: transparent;
                color: {ThemeManager.TEXT_PRIMARY};
                text-align: left;
                padding: 12px 16px;
                border: none;
                border-radius: {ThemeManager.BORDER_RADIUS}px;
                font-size: 14px;
            }}

            QPushButton:hover {{
                background-color: {ThemeManager.PRIMARY_COLOR};
                color: white;
            }}

            QPushButton:pressed {{
                background-color: {ThemeManager.PRIMARY_DARK};
                color: white;
            }}
            """
        )

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(12, 16, 12, 16)
        self._layout.setSpacing(8)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._build_menu()

    def _build_menu(self) -> None:
        """
        Construye el menú.
        """
        for module in self._registry.all():

            button = QPushButton(module.title)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(
                lambda _, module_id=module.id: self._router.navigate(module_id)
            )

            self._layout.addWidget(button)

            self._buttons[module.id] = button

        self._layout.addStretch()