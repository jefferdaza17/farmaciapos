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
from src.modules.inventory.inventory_page import InventoryPage
from src.modules.sales.sales_page import SalesPage
from src.modules.clients.clients_page import ClientsPage
from src.modules.purchases.purchases_page import PurchasesPage
from src.modules.reports.reports_page import ReportsPage
from src.modules.suppliers.suppliers_page import SuppliersPage
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

        self._launcher = Launcher(registry=self._registry, router=self._router)

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
        inventory = InventoryPage()
        sales = SalesPage()
        clients = ClientsPage()
        suppliers = SuppliersPage()
        purchases = PurchasesPage()
        reports = ReportsPage()

        self._registry.register(
            WorkspaceItem(id="home", title="Inicio", icon="home", order=1, page=home)
        )

        self._router.register(name="home", page=home)

        self._registry.register(
            WorkspaceItem(
                id="inventory",
                title="Inventario",
                icon="inventory",
                order=2,
                page=inventory,
            )
        )

        self._router.register(name="inventory", page=inventory)

        self._registry.register(
            WorkspaceItem(id="sales", title="Ventas", icon="sales", order=3, page=sales)
        )

        self._router.register(name="sales", page=sales)

        self._registry.register(
            WorkspaceItem(
                id="clients", title="Clientes", icon="clients", order=4, page=clients
            )
        )
        self._router.register(name="clients", page=clients)

        self._registry.register(
            WorkspaceItem(
                id="suppliers",
                title="Proveedores",
                icon="suppliers",
                order=5,
                page=suppliers,
            )
        )
        self._router.register(name="suppliers", page=suppliers)

        self._registry.register(
            WorkspaceItem(
                id="purchases",
                title="Compras",
                icon="purchases",
                order=6,
                page=purchases,
            )
        )
        self._router.register(name="purchases", page=purchases)

        self._registry.register(
            WorkspaceItem(
                id="reports", title="Reportes", icon="reports", order=7, page=reports
            )
        )
        self._router.register(name="reports", page=reports)

        self._router.navigate("home")
