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

from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from src.core.router import Router
from src.core.workspace_registry import WorkspaceItem
from src.core.workspace_registry import WorkspaceRegistry
from src.modules.home.home_page import HomePage
from src.ui.shell.launcher import Launcher
from src.ui.shell.top_bar import TopBar
from src.ui.shell.workspace import Workspace


class AppShell(QWidget):
    """
    Contenedor principal de la aplicación.
    """

    def __init__(self) -> None:
        """
        Inicializa la interfaz principal.
        """
        super().__init__()

        self._registry = WorkspaceRegistry()

        self._top_bar = TopBar()
        self._workspace = Workspace()
        self._router = Router(self._workspace)

        self._register_modules()

        self._launcher = Launcher(
            registry=self._registry,
            router=self._router
        )

        self._build_ui()

    @property
    def workspace(self) -> Workspace:
        """
        Retorna el Workspace.
        """
        return self._workspace

    @property
    def router(self) -> Router:
        """
        Retorna el Router.
        """
        return self._router

    @property
    def workspace_registry(self) -> WorkspaceRegistry:
        """
        Retorna el registro de módulos.
        """
        return self._registry

    def _build_ui(self) -> None:
        """
        Construye la interfaz principal.
        """
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        content_layout.addWidget(self._launcher)
        content_layout.addWidget(self._workspace, 1)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self._top_bar)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def _register_modules(self) -> None:
        """
        Registra los módulos iniciales.
        """
        home = HomePage()

        self._registry.register(
            WorkspaceItem(
                id="home",
                title="Inicio",
                icon="home",
                order=1,
                page=home
            )
        )

        self._router.register(
            name="home",
            page=home
        )

        self._router.navigate("home")